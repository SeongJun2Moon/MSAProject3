# 오류코드
### sqlalchemy.exc.DataError: (pymysql.err.DataError) (1366, "Incorrect string value)
- mysql 접속 후 아래코드 입력
```shell
ALTER DATABASE [DB명] CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
```
### OperationalError (1054, "Unknown column)
1. db에 특정 컬럼이 없음 초기화 후 진행.
2. 데이터 넣는 작업에서 replace -> append로 바꿈
