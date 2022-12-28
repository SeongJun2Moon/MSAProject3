import matplotlib.pyplot as plt
from keras.datasets import imdb
from sklearn.model_selection import train_test_split
import numpy as np
from keras import Sequential, layers, utils, optimizers, callbacks
import tensorflow as tf

import nltk
nltk.download('punkt')




class Imdb_model:
    def __init__(self):
        global train_input, train_target, test_input, test_target
        utils.set_random_seed(42)
        tf.config.experimental.enable_op_determinism()
        (train_input, train_target), (test_input, test_target) = imdb.load_data(num_words=500)

    def model_hook(self):
        self.check_data_set()
        self.preprocess()
        self.create_rnn_model()
        self.fit()

    def dataset_info(self):
        print(train_input.shape, test_input.shape)
        print(f"첫 번째 리뷰의 길이 : {len(train_input[0])}")
        print(f"두 번째 리뷰의 길이 : {len(train_input[1])}")
        print(f"첫 번째 리뷰의 내용 : {train_input[0]}")
        print(f"타깃 데이터(부정과 긍정) : {train_target[:20]}")

    def check_data_set(self):
        global train_input, val_input, train_target, val_target
        train_input, val_input, train_target, val_target = train_test_split(train_input, train_target, test_size=0.2,
                                                                            random_state=42)
        lengths = np.array([len(x) for x in train_input])
        # print(np.mean(lengths), np.median(lengths))
        # plt.hist(lengths)
        # plt.xlabel('length')
        # plt.ylabel('frequency')
        # plt.show()

    def preprocess(self):
        global train_seq, val_seq
        train_seq = utils.pad_sequences(train_input, maxlen=100)
        # print(train_seq.shape)
        # print(train_seq[0])
        # print(train_input[0][-10:])
        # print(train_seq[5])
        val_seq = utils.pad_sequences(val_input, maxlen=100)

    def create_rnn_model(self):
        global train_oh, val_oh, model
        model = Sequential()
        sample_length = 100
        freq_words = 500
        model.add(layers.SimpleRNN(8, input_shape=(sample_length, freq_words)))
        model.add(layers.Dense(1, activation='sigmoid'))
        train_oh = utils.to_categorical(train_seq)
        # print(train_oh.shape)
        # print(train_oh[0][0][:12])
        # print(np.sum(train_oh[0][0]))
        val_oh = utils.to_categorical(val_seq)
        # model.summary()
        return model

    def fit(self):
        rmsprop = optimizers.RMSprop(learning_rate=1e-4)
        model = self.create_rnn_model()
        model.compile(optimizers=rmsprop, loss='binary_crossentropy', metrics=['accuracy'])
        checkpoint_cb = callbacks.ModelCheckpoint('best-siplernn-model.h5', save_best_only=True)
        early_stopping_cb = callbacks.EarlyStopping(patience=3, restore_best_weights=True)
        history = model.fit(train_oh, train_target, epochs=100, batch_size=64, validation_data=(val_oh, val_target), callbacks=[checkpoint_cb, early_stopping_cb])

        plt.plot((history.history['loss']))
        plt.plot((history.history['val_loss']))
        plt.xlabel('epoch')
        plt.ylabel('loss')
        plt.legend(['train', 'val'])
        plt.show()
        print(train_seq.nbytes, train_oh.nbytes)

    # def use_word_embedding(self):
    #     model2 = Sequential()
    #     model2.add(layers.Embedding(500, 16, input_length=100))
    #     model2.add(layers.SimpleRNN(8))
    #     model2.add(layers.Dense(1, activation='sigmoid'))
    #     model2.summary()
    #     rmsprop = optimizers.RMSprop(learning_rate=1e-4)
    #     model2.compile(optimizer=rmsprop, loss='binary_crossentropy', metrics=['accuracy'])
    #     checkpoint_cb = callbacks.ModelCheckpoint('best-embedding-model.h5', save_best_only=True)
    #     early_stopping_cb = callbacks.EarlyStopping(patience=3, restore_best_weights=True)
    #     train_seq = self.train_seq
    #     train_target = self.train_target
    #     val_seq = self.val_seq
    #     val_target = self.val_target
    #     history = model2.fit(train_seq, train_target, epochs=100, batch_size=64, validation_data=(val_seq, val_target),
    #                          callbacks=[checkpoint_cb, early_stopping_cb])
    #     plt.plot((history.history['loss']))
    #     plt.plot((history.history['val_loss']))
    #     plt.xlabel('epoch')
    #     plt.ylabel('loss')
    #     plt.legend(['train', 'val'])
    #     plt.show()



if __name__ == '__main__':
    model = Imdb_model()
    model.model_hook()