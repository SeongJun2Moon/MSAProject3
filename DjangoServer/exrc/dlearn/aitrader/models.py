from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
import numpy as np
import pandas as pd
class SamsungKospi:
    def __init__(self):
        global kospi200, samsung
        kospi200 = np.load('C:/Users/SJMoon/AIA/MSAProject/DjangoServer/exrc/dlearn/aitrader/save/kospi200.npy', allow_pickle=True)
        samsung = np.load('C:/Users/SJMoon/AIA/MSAProject/DjangoServer/exrc/dlearn/aitrader/save/samsung.npy', allow_pickle=True)

    def hook(self):
        self.split_xy5(samsung, 5, 1)
        self.dataset()
        self.preprocessing()
        self.modeling()

    def csv_to_npy(self):
        df1 = pd.read_csv("C:/Users/SJMoon/AIA/MSAProject/DjangoServer/exrc/dlearn/aitrader/data/kospi200.csv", index_col=0,
                          header=0, encoding='UTF8', sep=',').drop('변동 %', axis=1)
        df2 = pd.read_csv("C:/Users/SJMoon/AIA/MSAProject/DjangoServer/exrc/dlearn/aitrader/data/samsung.csv", index_col=0,
                          header=0, encoding='UTF8', sep=',').drop('변동 %', axis=1).dropna()
        for i in range(len(df1.index)):
            df1.iloc[i, 4] = float(df1.iloc[i, 4].replace('M', '').replace('K', ''))

        for i in range(len(df2.index)):
            for j in range(len(df2.iloc[i]) - 1):
                df2.iloc[i, j] = int(df2.iloc[i, j].replace(',', ''))
        for i in range(len(df2.index)):
            df2.iloc[i, 4] = float(df2.iloc[i, 4].replace('M', '').replace('K', ''))

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
            y_end_numbber = x_end_number + y_column

            if y_end_numbber > len(dataset):
                break
            tmp_x = dataset[i:x_end_number, :]
            tmp_y = dataset[x_end_number:y_end_numbber, 3]
            x.append(tmp_x)
            y.append(tmp_y)
        return np.array(x), np.array(y)

    def dataset(self):
        global x_train, x_test, y_train, y_test
        x, y = SamsungKospi().split_xy5(samsung, 5, 1)
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, random_state=1, test_size=0.3)

        # y_train = y_train.reshape(x_train.shape[0], x_train[1], 1).astype(np.float32)
        # y_test = y_test.reshape(x_train.shape[0], x_train[1], 1).astype(np.float32)
        print(x_train.shape)
        print(x_test.shape)
        print(y_train.shape)
        print(y_test.shape)

        # standarScaler 에서 2차원으로 받기 때문에 3차원을 2차원으로 바꿔줌
        x_train = np.reshape(x_train,
                             (x_train.shape[0], x_train.shape[1] * x_train.shape[2]))
        x_test = np.reshape(x_test,
                            (x_test.shape[0], x_test.shape[1] * x_test.shape[2]))
        print(x_train.shape)
        print(x_test.shape)

    def preprocessing(self):
        global x_train_scaled, x_test_scaled
        scaler = StandardScaler()
        scaler.fit(x_train)
        x_train_scaled = scaler.transform(x_train)
        x_test_scaled = scaler.transform(x_test)
        print(x_train_scaled[0, :])

    def modeling(self):
        global model
        model = Sequential()
        model.add(Dense(64, input_shape=(25,)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))

        model.compile(loss='mse', optimizer='adam', metrics=['mse'])

        early_stopping = EarlyStopping(patience=20)
        model.fit(x_train_scaled, y_train.astype(np.float32), validation_split=0.2, verbose=1,
                  batch_size=1, epochs=100, callbacks=[early_stopping])

        loss, mse = model.evaluate(x_test_scaled, y_test.astype(np.float32), batch_size=1)
        print('loss : ', loss)
        print('mse : ', mse)

        y_pred = model.predict(x_test_scaled)

        # for i in range(5):
        #     print('종가 : ', y_test[i][0], '/ 예측가 : ', y_pred[i][0])
        return [{'종가' : y_test[i][0], '예측가' : y_pred[i][0]} for i in range(5)]

    def save_model(self):
        file_name = "C:/Users/SJMoon/AIA/MSAProject/DjangoServer/exrc/dlearn/aitrader/save/samsung_stock_dnn_model.h5"
        print(f"저장경로: {file_name}")
        model.save(file_name)

if __name__ == '__main__':
    SamsungKospi().hook()