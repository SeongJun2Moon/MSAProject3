# 데이터프레임 mysql로 보내기 - service.py
### db연결 라이브러리 설치
1. sqlalchemy
   - 라이브러리 설치 : pip install sqlalchemy
   - 임포트 : from sqlalchemy import create_engine
   - db_connection = create_engine('mysql+pymysql://[db유저이름]:[db패스워드]@[로컬호스트주소]/[데이터베이스이름]').connect()
2. pymysql
   - 라이브러리 설치 : pip install pymysql
   - 임포트 : import pymysql
### 랜덤 id 만드는 라이브러리가 있다
- 라이브러리 설치 : pip install random-id
- 임포트 : from random_id import *
- id = random_id(length=4, character_set=string.digits)

### 데이터프레임 생성
- df = pd.DataFrame(zip([리스트들]), index=[행의 길이만큼], columns=[칼럼이름들])

### 데이터베이스 연결
- db_connection = create_engine('mysql+pymysql://root:root@localhost:3306/mydb)

### mysql에 저장
- df.to_sql(name='[테이블이름]', con=db_connection, if_exists='[추가/교체]', index=False)

### 오류
- 버전오류 : pip install --upgrade sqlalchemy
- pymysql.err.OperationalError - 1054 : if_exists='replace' - 테이블이 비어있거나 키값이 다를 때
- sqlalchemy.exc.IntegrityError - 1217 : if_exists='append' - 온전한 테이블에 내용을 추가할 때