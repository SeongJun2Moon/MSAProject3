from sqlalchemy import create_engine
import pymysql
from random_id import *
import pandas as pd


class UserService:
    def __init__(self):
        self.id_lst = list(i for i in range(1, 101))
        self.nickname_lst = list(random_id() for i in range(100))
        self.email_lst = list(f"{i}@gmail.com" for i in self.nickname_lst)
        self.pw_lst = list(1 for i in range(100))
        self.df = None

    def hook_db(self):
        self.create_df()
        self.connect_db()

    def hook_react(self):
        self.create_df()

    def create_df(self):
        # 데이터프레임 생성
        df = pd.DataFrame(zip(self.id_lst, self.email_lst, self.nickname_lst, self.pw_lst),
                          index=[i for i in range(len(self.nickname_lst))], columns=["blog_id", "email", "nickname", "password"])
        self.df = df

    def connect_db(self):
        # 데이터베이스 연결
        db_connection = create_engine('mysql+pymysql://root:root@localhost:3306/mydb').connect()

        # mysql에 저장
        self.df.to_sql(name='users', con=db_connection, if_exists='replace', index=False)



if __name__ == '__main__':
    UserService().hook_db()