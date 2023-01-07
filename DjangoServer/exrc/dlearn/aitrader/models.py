from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras import Input
from keras.models import Sequential, Model
from keras.layers import Dense, LSTM, concatenate
from keras.callbacks import EarlyStopping
from enum import Enum
import numpy as np
import pandas as pd
from abc import abstractmethod, ABCMeta

class ModelType(Enum):
    dnn_model = 1
    dnn_ensemble = 2
    lstm_model = 3
    lstm_ensemble = 4

class H5FileNames(Enum):
    dnn_model = "samsung_stock_dnn_model.h5"
    dnn_ensemble = "samsung_stock_dnn_ensemble.h5"
    lstm_model = "samsung_stock_lstm_model.h5"
    lstm_ensemble = "samsung_stock_lstm_ensemble.h5"

class AiTradeBase(metaclass=ABCMeta):
    @abstractmethod
    def file_checker(self):
        pass
    @abstractmethod
    def normalization(self, df):
        pass
    @abstractmethod
    def csv_to_npy(self):
        pass
    @abstractmethod
    def split_xy5(self, dataset, time_steps, y_column):
        pass
    @abstractmethod
    def DNN_scaled(self, dataset):
        pass
    @abstractmethod
    def LSTM_scaled(self, dataset):
        pass


class AiTradeModel(AiTradeBase):
    def __init__(self):
        global kospi200, samsung, model_save
        kospi200 = np.load('C:/Users/SJMoon/AIA/MSAProject/DjangoServer/exrc/dlearn/aitrader/save/kospi200.npy', allow_pickle=True)
        samsung = np.load('C:/Users/SJMoon/AIA/MSAProject/DjangoServer/exrc/dlearn/aitrader/save/samsung.npy', allow_pickle=True)
        model_save = "C:/Users/SJMoon/AIA/MSAProject/DjangoServer/exrc/dlearn/aitrader/save/"

    def file_checker(self):
        print(samsung[0])

    def normalization(self, df):
        df2 = df
        for i in range(len(df2.index)):
            for j in range(len(df2.iloc[i])):
                if "M" in df2.iloc[i, j]:
                    df2.iloc[i, j] = df2.iloc[i, j].replace(',', '')
                    df2.iloc[i, j] = df2.iloc[i, j].replace('M', '')
                    df2.iloc[i, j] = float(df2.iloc[i, j])
                    df2.iloc[i, j] = df2.iloc[i, j] * 1000000
                elif "K" in df2.iloc[i, j]:
                    df2.iloc[i, j] = df2.iloc[i, j].replace(',', '')
                    df2.iloc[i, j] = df2.iloc[i, j].replace('K', '')
                    df2.iloc[i, j] = float(df2.iloc[i, j])
                    df2.iloc[i, j] = df2.iloc[i, j] * 1000
                else:
                    df2.iloc[i, j] = df2.iloc[i, j].replace(',', '')
                    df2.iloc[i, j] = float(df2.iloc[i, j])

    def csv_to_npy(self):
        df1 = pd.read_csv("C:/Users/SJMoon/AIA/MSAProject/DjangoServer/exrc/dlearn/aitrader/data/kospi200.csv", index_col=0,
                          header=0, encoding='UTF8', sep=',').drop('변동 %', axis=1)
        df2 = pd.read_csv("C:/Users/SJMoon/AIA/MSAProject/DjangoServer/exrc/dlearn/aitrader/data/samsung.csv", index_col=0,
                          header=0, encoding='UTF8', sep=',').drop('변동 %', axis=1)

        df1 = df1.astype('str')
        df1.replace(np.nan, '0', regex=True, inplace=True)
        df2.replace(np.nan, '0', regex=True, inplace=True)

        df1 = df1[df1['거래량'] != '0']
        df2 = df2[df2['거래량'] != '0']

        self.normalization(df1)
        self.normalization(df2)

        df1 = df1.sort_values(['날짜'], ascending=[True])
        df2 = df2.sort_values(['날짜'], ascending=[True])
        df1 = df1.values
        df2 = df2.values

        np.save('./save/kospi200.npy', arr=df1)
        np.save('./save/samsung.npy', arr=df2)


    def split_xy5(self, dataset, time_steps, y_column):
        x,y = list(), list()
        for i in range(len(dataset)):
            x_end_number = i + time_steps
            y_end_number = x_end_number + y_column

            if y_end_number > len(dataset):
                break
            tmp_x = dataset[i:x_end_number, :]
            tmp_y = dataset[x_end_number:y_end_number, 3]
            x.append(tmp_x)
            y.append(tmp_y)
        return np.array(x), np.array(y)

    def DNN_scaled(self, dataset):
        x, y = self.split_xy5(dataset, 5, 1)
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, random_state=1, test_size=0.3)

        # print(x_train.shape)
        # print(x_test.shape)
        # print(y_train.shape)
        # print(y_test.shape)

        # standarScaler 에서 2차원으로 받기 때문에 3차원을 2차원으로 바꿔줌
        x_train = np.reshape(x_train,(x_train.shape[0], x_train.shape[1] * x_train.shape[2])).astype(float)
        x_test = np.reshape(x_test,(x_test.shape[0], x_test.shape[1] * x_test.shape[2])).astype(float)
        y_train = y_train.astype(float)
        y_test = y_test.astype(float)
        print(x_train.shape)
        print(x_test.shape)

        scaler = StandardScaler()
        scaler.fit(x_train)
        x_train_scaled = scaler.transform(x_train).astype(float)
        x_test_scaled = scaler.transform(x_test).astype(float)
        print(x_train_scaled[0, :])
        return x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled

    def LSTM_scaled(self, dataset):
        x,y = self.split_xy5(dataset, 5, 1)
        # print(x.shape) #(16, 5, 5)
        # print(y.shape) #(16, 1)

        x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=1, test_size=0.3)
        # print(x_train.shape) #(11, 5, 5)
        # print(x_test.shape) #(5, 5, 5)
        # print(y_train.shape) #(11, 1)
        # print(y_test.shape) #(5, 1)

        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1]*x_train.shape[2])).astype(float)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1]*x_test.shape[2])).astype(float)
        y_train = y_train.astype(float)
        y_test = y_test.astype(float)

        scalar = StandardScaler()
        scalar.fit(x_train)
        x_train_scaled = scalar.transform(x_train)
        x_test_scaled = scalar.transform(x_test)
        # print(x_train_scaled[0,:])
        # print(x_test_scaled.shape) #(5, 25)
        x_train_scaled = np.reshape(x_train_scaled, (x_train_scaled.shape[0], 5, 5)).astype(float)
        x_test_scaled = np.reshape(x_test_scaled, (x_test_scaled.shape[0], 5, 5)).astype(float)
        return x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled

class DNNModel(AiTradeModel):
    def create(self):
        x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = self.DNN_scaled(samsung)

        print(x_train_scaled[0, :])
        print(x_test_scaled.shape)
        model = Sequential()
        model.add(Dense(64, input_shape=(25,)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))
        model.compile(loss='mse', optimizer='adam', metrics=['mse'])
        early_stopping = EarlyStopping(patience=20)
        model.fit(x_train_scaled, y_train, validation_split=0.2, verbose=1, batch_size=1, epochs=100,
                  callbacks=[early_stopping])
        loss, mse = model.evaluate(x_test_scaled, y_test, batch_size=1)
        print('loss : ', loss)
        print('mse: ', mse)
        y_pred = model.predict(x_test_scaled)
        for i in range(5):
            print(f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}')
        model.save(model_save + "DNN.h5")

class LSTMModel(AiTradeModel):
    def create(self):
        x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = self.LSTM_scaled(samsung)

        print(x_train_scaled.shape) #(11, 5, 5)
        print(x_test_scaled.shape) #(5, 5, 5)

        model = Sequential()
        model.add(LSTM(64, input_shape=(5, 5)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))
        model.compile(loss='mse', optimizer='adam', metrics=['mse'])

        early_stopping = EarlyStopping(patience=20)
        model.fit(x_train_scaled, y_train, validation_split=0.2, verbose=1, batch_size=1, epochs=100,
                  callbacks=[early_stopping])
        loss, mse = model.evaluate(x_test_scaled, y_test, batch_size=1)

        print('loss : ', loss)
        print('mse: ', mse)
        y_pred = model.predict(x_test_scaled)
        for i in range(5):
            print(f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}')
        model.save(model_save + "LSTM.h5")

class DNNEnsemble(AiTradeModel):
    def create(self):
        x1_train, x1_test, y1_train, y1_test, x1_train_scaled, x1_test_scaled = self.DNN_scaled(samsung)
        x2_train, x2_test, y2_train, y2_test, x2_train_scaled, x2_test_scaled = self.DNN_scaled(kospi200)

        input1 = Input(shape=(25,))
        dense1 = Dense(64)(input1)
        dense1 = Dense(32)(dense1)
        dense1 = Dense(32)(dense1)
        output1 = Dense(32)(dense1)
        input2 = Input(shape=(25,))
        dense2 = Dense(64)(input2)
        dense2 = Dense(32)(dense2)
        dense2 = Dense(32)(dense2)
        output2 = Dense(32)(dense2)

        merge = concatenate([output1, output2])
        output3 = Dense(1)(merge)
        model = Model(inputs=[input1, input2], outputs=output3)

        model.compile(loss='mse', optimizer='adam', metrics=['mse'])
        early_stopping = EarlyStopping(patience=20)
        model.fit([x1_train_scaled, x2_train_scaled], y1_train, validation_split=0.2,
                  verbose=1, batch_size=1, epochs=100,
                  callbacks=[early_stopping])

        loss, mse = model.evaluate([x1_test_scaled, x2_test_scaled], y1_test, batch_size=1)

        print('loss : ', loss)
        print('mse : ', mse)

        y1_pred = model.predict([x1_test_scaled, x2_test_scaled])

        for i in range(5):
            print('종가 : ', y1_test[i], '/ 예측가 : ', y1_pred[i])

        model.save(model_save + "DNN_Ensemble.h5")

class LSTMEnsemble(AiTradeModel):
    def create(self):
        x1_train, x1_test, y1_train, y1_test, x1_train_scaled, x1_test_scaled = self.LSTM_scaled(samsung)
        x2_train, x2_test, y2_train, y2_test, x2_train_scaled, x2_test_scaled = self.LSTM_scaled(kospi200)

        input1 = Input(shape=(5, 5))
        dense1 = LSTM(64)(input1)
        dense1 = Dense(32)(dense1)
        dense1 = Dense(32)(dense1)
        output1 = Dense(32)(dense1)

        input2 = Input(shape=(5, 5))
        dense2 = LSTM(64)(input2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        output2 = Dense(32)(dense2)

        merge = concatenate([output1, output2])
        output3 = Dense(1)(merge)

        model = Model(inputs=[input1, input2], outputs=output3)

        model.compile(loss='mse', optimizer='adam', metrics=['mse'])

        early_stopping = EarlyStopping(patience=20)
        model.fit([x1_train_scaled, x2_train_scaled], y1_train, validation_split=0.2,
                  verbose=1, batch_size=1, epochs=100,
                  callbacks=[early_stopping])

        loss, mse = model.evaluate([x1_test_scaled, x2_test_scaled], y1_test, batch_size=1)

        print('loss : ', loss)
        print('mse : ', mse)

        y1_pred = model.predict([x1_test_scaled, x2_test_scaled])

        for i in range(5):
            print('종가 : ', y1_test[i], '/ 예측가 : ', y1_pred[i])

        model.save(model_save + "LSTM_Ensemble.h5")


if __name__ == '__main__':
    AiTradeModel().DNN_scaled()