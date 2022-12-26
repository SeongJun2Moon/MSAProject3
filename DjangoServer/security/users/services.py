import random
import pandas as pd
from sqlalchemy import create_engine

from util.algorithm.lambdas import lambda_string, lambda_k_name, lambda_phone, \
    lambda_birth, address_list, job_list, interests_list


class UserService(object):
    def __init__(self):
        global engine
        engine = create_engine(
            "mysql+pymysql://root:root@localhost:3306/mydb",
            encoding='utf-8').connect()

    '''
     model의 dtype이 숫자인 AutoField로 돼있어서 임시로 수정되면 
     "blog_userid= ''.join(random.sample(string_pool, 5))"로 변경
     (email도 email = blog_userid + "@naver.com"로 변경)
    '''
    def create_user(self)->[]:
        user_email = str(lambda_string(4)) + "@test.com"
        password = '1'
        user_name = lambda_k_name(2)
        phone = lambda_phone(4)
        birth = lambda_birth(1985, 2011)
        address = random.choice(address_list)
        job = random.choice(job_list)
        user_interests = random.choice(interests_list)
        token = 'JWT fefege..'
        '''
        user_email = models.TextField()
        password = models.CharField(max_length=10)
        user_name = models.TextField()
        phone = models.TextField()
        birth = models.TextField()
        address = models.TextField(blank=True)
        job = models.TextField()
        user_interests = models.TextField()
        '''
        return [user_email, password, user_name, phone, birth,
                address, job, user_interests, token]


    def create_users(self)->[]:
        rows = [self.create_user() for i in range(100)]
        columns = ['user_email', 'password', 'user_name', 'phone', 'birth', 'address', 'job', 'user_interests', 'token']
        df = pd.DataFrame(rows, columns=columns)
        df['user_email'] = df['user_email'].astype(str)
        print(df)
        return df


    def insert_users(self):
        df = self.create_users()
        df.to_sql(name='users',
                  if_exists='replace', # append, replace, fail
                  con=engine,
                  index=False)

    def show_users(self):
        df = self.create_users()
        user_email = list(df.to_dict()['user_email'].values())
        password = list(df.to_dict()['password'].values())
        user_name = list(df.to_dict()['user_name'].values())
        phone = list(df.to_dict()['phone'].values())
        birth = list(df.to_dict()['birth'].values())
        address = list(df.to_dict()['address'].values())
        job = list(df.to_dict()['job'].values())
        user_interests = list(df.to_dict()['user_interests'].values())
        token = list(df.to_dict()['token'].values())
        users_json = [{"id": int(i + 1), "user_email": str(user_email), "password": str(password), "user_name": str(user_name),
                       "phone": str(phone), "birth": str(birth), "address": str(address), "job" : str(job),
                       "user_interests" : str(user_name), "token" : str(token)} for i, (user_email, password, user_name, phone, birth,
                                                                             address, job, user_interests, token)
                      in enumerate(zip(user_email, password, user_name, phone, birth, address, job, user_interests, token))]
        return users_json

    def userid_checker(self):  # 아이디 중복체크
        pass
        '''print('중복 확인')
        df = self.create_users()
        if df.duplicated(['blog_userid'], keep=False) == True:
            print('중복된 아이디입니다')
        else:
            return df'''


if __name__ == '__main__':
    UserService().insert_users()