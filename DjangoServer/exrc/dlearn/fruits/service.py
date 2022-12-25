import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow import keras
from keras.callbacks import ModelCheckpoint

class FruitsService:

    def __init__(self):
        self.class_names = None
        self.trainpath = "C:/Users/MSJ/AIA/MsaProject/DjangoServer/shop/fruits/fruits-360-5/Training"
        self.testpath = "C:/Users/MSJ/AIA/MsaProject/DjangoServer/shop/fruits/fruits-360-5/Test"
        self.AppleBraeburnTest = f"{self.testpath}/Apple Braeburn"
        self.AppleCrimsonSnowTest = f"{self.testpath}/Apple Crimson Snow"
        self.AppleGolden1Test = f"{self.testpath}/Apple Golden 1"
        self.AppleGolden2Test = f"{self.testpath}/Apple Golden 2"
        self.AppleGolden3Test = f"{self.testpath}/Apple Golden 3"
        self.AppleBraeburnTrain = f"{self.trainpath}/Apple Braeburn"
        self.AppleCrimsonSnowTrain = f"{self.trainpath}/Apple Crimson Snow"
        self.AppleGolden1Train = f"{self.trainpath}/Apple Golden 1"
        self.AppleGolden2Train = f"{self.trainpath}/Apple Golden 2"
        self.AppleGolden3Train = f"{self.trainpath}/Apple Golden 3"
        self.batch_size = 32
        self.img_height = 100
        self.img_width = 100
        self.train_ds = None
        self.val_ds = None
        self.test_ds = None
        self.test_ds1 = None
        self.model = None
        self.history = None

    def hook_ds(self):
        self.create_train_ds()
        self.create_validation_ds()
        self.lable()
        self.dataset_test()
        self.get_img_ds()
        self.modify_ds_to_prefetch()
        self.model_compile()
        self.learning()
        self.show_grape()
        self.show_persentage()

    def hook_ds_shuffle_false(self):
        self.create_train_ds()
        self.create_validation_ds()
        self.lable()
        self.dataset_test()
        self.get_img_ds_shuffle_false()
        self.modify_ds_to_prefetch()
        self.model_compile()
        self.learning()
        self.show_grape()
        self.show_persentage()

    def show_apple(self):
        img = tf.keras.preprocessing.image.load_img \
            (f'{self.AppleGolden3Train}/0_100.jpg')
        plt.imshow(img)
        plt.axis("off")
        plt.show()

    def create_train_ds(self):
        # 원본 학습 데이터셋을 불러오기
        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            self.trainpath,
            validation_split=0.3,
            subset="training",
            seed=1,
            image_size=(self.img_height, self.img_width),
            batch_size=self.batch_size)
        self.train_ds = train_ds

    def create_validation_ds(self):
        # 원본 학습 데이터넷에서 검증 데이터셋을 분리
        val_ds = tf.keras.preprocessing.image_dataset_from_directory(
            self.trainpath,
            validation_split=0.3,
            subset="validation",
            seed=1,
            image_size=(self.img_height, self.img_width),
            batch_size=self.batch_size)
        self.val_ds = val_ds

    def lable(self):
        # 불러온 학습 데이터엣에서 레이블 값(여기서는 5개 사과 품종)을 확인
        class_names = self.train_ds.class_names
        print(class_names)
        self.class_names = class_names

    def dataset_test(self):
        # 원본 테스트 데이터셋 불러오기
        test_ds = tf.keras.preprocessing.image_dataset_from_directory(
            self.testpath,
            seed=1,
            image_size=(self.img_height, self.img_width),
            batch_size=self.batch_size)
        self.test_ds = test_ds

        # 원본 테서트 데이터셋을 shuffle=False 옵션 추가하여 데이터셋 test_ds1을 별도로 생성
        test_ds1 = tf.keras.preprocessing.image_dataset_from_directory(
            self.testpath,
            seed=1,
            image_size=(self.img_height, self.img_width),
            batch_size=self.batch_size,
            shuffle=False)
        self.test_ds1 = test_ds1

    def get_img_ds(self):
        # test_ds에서 레이블 정보만 추출하여 y에 저장
        y = np.concatenate([y for x, y in self.test_ds], axis=0)
        # print(y)

        # test_ds1에서 이미지 정보만 추출하여 x에 저장
        x = np.concatenate([x for x, y in self.test_ds], axis=0)
        # print(x[0])

        # test_ds의 첫번째 이미지와 레이블을 불러와 그림으로 확인
        plt.figure(figsize=(3, 3))
        plt.imshow(x[int(input("사과숫자: "))].astype("uint8"))
        plt.title(self.class_names[y[0]])
        plt.axis("off")
        plt.show()

    def get_img_ds_shuffle_false(self):
        # test_ds1에서 레이블 정보만 추출하여 y에 저장
        y = np.concatenate([y for x, y in self.test_ds1], axis=0)
        # print(y)

        # test_ds1에서 이미지 정보만 추출하여 x에 저장
        x = np.concatenate([x for x, y in self.test_ds1], axis=0)
        # print(x[0])

        # test_ds1의 마지막 이미지와 레이블을 불러와 그림으로 확인
        plt.figure(figsize=(3, 3))
        plt.imshow(x[int(input("사과숫자: "))].astype("uint8"))
        plt.title(self.class_names[y[-1]])
        plt.axis("off")
        plt.show()

    def modify_ds_to_prefetch(self):
        # test_ds1을 제외하고 위에서 불러온 세가지 데이터셋을 Prefetch 데이터셋으로 설정
        BUFFER_SIZE = 10000
        AUTOTUNE = tf.data.experimental.AUTOTUNE

        train_ds = self.train_ds.cache().shuffle(BUFFER_SIZE).prefetch(buffer_size=AUTOTUNE)
        val_ds = self.val_ds.cache().prefetch(buffer_size=AUTOTUNE)
        test_ds = self.test_ds.cache().prefetch(buffer_size=AUTOTUNE)

        # 합성곱 신경망(CNN) 모델 구성
        num_classes = 5
        model = tf.keras.Sequential([
            keras.layers.experimental.preprocessing.Rescaling(1. / 255, input_shape=(self.img_height, self.img_width, 3)),
            keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
            keras.layers.MaxPooling2D(2),
            keras.layers.Dropout(.50),
            keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
            keras.layers.MaxPooling2D(2),
            keras.layers.Dropout(.50),
            keras.layers.Flatten(),
            keras.layers.Dense(500, activation='relu'),
            keras.layers.Dropout(.50),
            keras.layers.Dense(num_classes, activation='softmax')
        ])
        model.summary()
        self.model = model

    def model_compile(self):
        # 모델을 컴파일
        self.model.compile(
            optimizer='adam',
            loss=tf.losses.SparseCategoricalCrossentropy(),
            metrics=['accuracy'])

    def learning(self):
        checkpointer = ModelCheckpoint('save/CNNClassifier.h5', save_best_only=True)
        early_stopping_cb = keras.callbacks.EarlyStopping(patience=5, monitor='val_accuracy',
                                                          restore_best_weights=True)

        # 모델을 학습
        epochs = 20
        history = self.model.fit(
            self.train_ds,
            batch_size=self.batch_size,
            validation_data=self.val_ds,
            epochs=epochs,
            callbacks=[checkpointer, early_stopping_cb]
        )
        self.history = history

    def show_grape(self):
        # 매 epochs마다 모델 정확도와 손실을 그래프로 그리기

        acc = self.history.history['accuracy']  # 모델의 학습 정확도를 변수 acc에 저장
        val_acc = self.history.history['val_accuracy']  # 모델의 검증 정확도를 변수 val_acc에 저장

        loss = self.history.history['loss']  # 모델의 학습 손실을 변수 loss에 저장
        val_loss = self.history.history['val_loss']  # 모델의 검증 손실을 변수 val_loss에 저장

        # epochs가 14회가 아닌 다른 결과(예:10회)로 나오면 아래 줄 14를 해당 숫자인 10로 바꿔주야 함에 유의
        epochs_range = range(1, len(loss)+1)  # epochs가 14회까지만 수행된 것을 반영

        # 학습 정확도와 검증 정확도를 그리기
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        # 학습 손실와 검증 손실을 그리기
        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')
        plt.show()

    def show_persentage(self):
        # model.fit() 실행시 검증 정확도가 가장 높은 에포크에 해당하는 모델 가중치 계수들을 불러오기
        self.model.load_weights('save/CNNClassifier.h5')

        # 데이터셋 test_ds를 사용하여 모델을 평가
        test_loss, test_acc = self.model.evaluate(self.test_ds)

        print("test loss: ", test_loss)
        print()
        print("test accuracy: ", test_acc)

        # test_ds1의 첫번째 이미지의 예측 결과
        predictions = self.model.predict(self.test_ds1)
        score = tf.nn.softmax(predictions[0])
        print(
            "This image most likely belongs to {} with a {:.2f} percent confidence."
            .format(self.class_names[np.argmax(score)], 100 * np.max(score))
        )
        score = tf.nn.softmax(predictions[-1])
        print(
            "This image most likely belongs to {} with a {:.2f} percent confidence."
            .format(self.class_names[np.argmax(score)], 100 * np.max(score))
        )

fashion_menu = ["Exit", #0
                "hook_ds",#1
                "hook_ds1",#2
            ]
fashion_lambda = {
    "1" : lambda x: x.hook_ds(),
    "2" : lambda x: x.hook_ds_shuffle_false()
            }
if __name__ == '__main__':
    service = FruitsService()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(fashion_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                fashion_lambda[menu](service)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")