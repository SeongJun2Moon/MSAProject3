# 목록
## 수업이론
- <a href="https://github.com/SeongJun2Moon/MSAProject/tree/main/DjangoServer/이론/cv.md">이미지분석이론</a>
- <a href="https://github.com/SeongJun2Moon/MSAProject/tree/main/DjangoServer/이론/cv와 plt RGB오류.md">cv와 plt RGB오류</a>
- <a href="https://github.com/SeongJun2Moon/MSAProject/tree/main/DjangoServer/이론/cv이미지읽기.md">cv이미지읽기</a>
- <a href="https://github.com/SeongJun2Moon/MSAProject/tree/main/DjangoServer/이론/이론.md">이론</a>
- <a href="https://github.com/SeongJun2Moon/MSAProject/tree/main/DjangoServer/이론/텐서플로 버전1 샘플코드.md">텐서플로 버전1 샘플코드</a>
- <a href="https://github.com/SeongJun2Moon/MSAProject/tree/main/DjangoServer/이론/함수형그래프 개요.md">함수형그래프 개요</a>
- <a href="https://github.com/SeongJun2Moon/MSAProject/tree/main/DjangoServer/이론/is-a,has-a.md">is-a, has-a</a>

## 코드 내 이론
### blog
- <a href="https://github.com/SeongJun2Moon/MSAProject/tree/main/DjangoServer/blog/busers">db로 데이터프레임 보내기</a>

### exrc.dlearn
- <a href="https://github.com/SeongJun2Moon/MSAProject/tree/main/DjangoServer/exrc/dlearn/fruits">과일분류 깃허브 및 에러</a>
1. 깃허브
2. 에러
  - ValueError: x and y must have same first dimension, but have shapes (14,) and (10,)

### exrc.nlp
- <a href="https://github.com/SeongJun2Moon/MSAProject/tree/main/DjangoServer/exrc/nlp/samsung_report">삼성리포트 세팅 및 오류</a>
1. MVC모델 패키지 세팅
2. 에러
   - systemerror: java.nio.file.invalidpathexception - 버전/경로 에러
   - Resource punkt not found. - NLTK 다운이 잘 안됨
   - oserror: cannot open resource - 워드클라우드 폰트 설정
   - TypeError - Object of type ‘int64’ is not JSON serializable : 자료구조 내 원소 int64타입을 인식 못함

### security.users
- <a href="https://github.com/SeongJun2Moon/MSAProject/tree/main/DjangoServer/security/users">유저스 에러</a>
1. 에러 : sqlalchemy.exc.DataError: (pymysql.err.DataError) (1366, "Incorrect string value)
###### mysql 접속 후 아래코드 입력
```shell
ALTER DATABASE [DB명] CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
```