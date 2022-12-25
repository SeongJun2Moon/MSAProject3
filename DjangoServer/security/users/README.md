# 오류코드
### sqlalchemy.exc.DataError: (pymysql.err.DataError) (1366, "Incorrect string value)
- mysql 접속 후 아래코드 입력
```shell
ALTER DATABASE [DB명] CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
```