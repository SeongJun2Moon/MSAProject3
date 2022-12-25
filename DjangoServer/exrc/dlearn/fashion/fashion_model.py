import keras.datasets.fashion_mnist
from matplotlib import pyplot as plt
import pandas as pd
import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
import os


class FashionModel:

    def create_model(self):
        (train_images, train_labels), (test_images, test_labels) = keras.datasets.fashion_mnist.load_data()
        plt.figure()
        plt.imshow(train_images[i])
        plt.colorbar()
        plt.grid(False)
        plt.show()
        # 모델구축
        model = Sequential([
            keras.layers.Flatten(input_shape=(28,28)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(10, activation='softmax')
        ])
        # 손실함수
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        model.fit(train_images, train_labels, epochs=5)
        test_loss, test_acc = model.evaluate(test_images, test_labels)
        print(f"Test Accuracy is {test_acc}")
        file_name = os.path.join(os.path.abspath("save"), "fashion_model.h5")
        model.save(file_name)
        return model



fashion_menu = ["Exit", #0
                "create_model",#1
            ]
fashion_lambda = {
    "1" : lambda x: x.create_model()
            }
if __name__ == '__main__':
    fasion = FashionModel()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(fashion_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                fashion_lambda[menu](fasion)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")

