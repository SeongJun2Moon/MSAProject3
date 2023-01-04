from keras.saving.save import load_model

from exrc.dlearn.aitrader.models import SamsungKospi, DNNModel, DNNEnsemble, LSTMModel, LSTMEnsemble
aitraders_menu = ["Exit", #0
                "DNNModel",#1
                "DNN Ensemble",#1
                "LSTMModel",#1
                "LSTM Ensemble",#1
            ]


if __name__ == '__main__':
    model = SamsungKospi()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(aitraders_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                if menu == "1":
                    DNNModel().create()
                elif menu == "2":
                    DNNEnsemble().create()
                elif menu == "3":
                    LSTMModel().create()
                elif menu == "4":
                    LSTMEnsemble().create()
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")