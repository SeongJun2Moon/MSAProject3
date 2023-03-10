from tensorflow import keras
import matplotlib.pyplot as plt
from pathlib import Path
import cv2 as cv

class MyFashion(keras.Model):
    def __init__(self):
        pass

    def exec(self):
        (train_input, train_target), (train_input, train_target) = keras.datasets.fashion_mnist.load_data()
        fig, axs = plt.subplots(1, 10, figsize=(10, 10))
        for i in range(10):
            axs[i].imshow(train_input[i], cmap='gray_r')
            axs[i].axis('off')

        fn = "{}.png".format("fashion2")
        plt.savefig(fn)
        target = cv.imread(fn)
        target = cv.resize(target, (1000, 500))
        dir = r"C:\Users\MSJ\AIA\ReactProject\multiplex\src\img"
        cv.imwrite(dir+r"\fasion.png", target)
        plt.show()

if __name__ == '__main__':
    m = MyFashion()
    m.exec()