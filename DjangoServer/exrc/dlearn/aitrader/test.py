from keras.saving.save import load_model

from exrc.dlearn.aitrader.models import SamsungKospi

class TestModel:

    def __init__(self):
        global DNN, DNN_Ensemble, LSTM, LSTM_Ensemble
        rute = "C:/Users/SJMoon/AIA/MSAProject/DjangoServer/exrc/dlearn/aitrader/save/"
        DNN = load_model(rute+"DNN.h5")
        DNN_Ensemble = load_model(rute+"DNN_Ensemble.h5")
        LSTM = load_model(rute+"LSTM.h5")
        LSTM_Ensemble = load_model(rute+"LSTM_Ensemble.h5")

    def hook(self):
        print("hi")




aitraders_menu = ["Exit", #0
                "Hook",#1
            ]
aitraders_lambda = {
    "1" : lambda x: x.hook()
            }
if __name__ == '__main__':
    ai = TestModel()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(aitraders_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                aitraders_lambda[menu](ai)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")