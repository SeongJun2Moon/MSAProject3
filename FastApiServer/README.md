### fastapi 설치
```shell
pip install fastapi 'uvicorn[standard]'
```
### uvicorn 설치
```shell
pip install uvicorn
```
### 실행명령어
```shell
python -m uvicorn main:api --reload 
```
### 보안 추가 설정(파이참에서 컴포즈 할 때 mysql 서버 연결 오류 뜨면)
```shell
grant all privileges on *.* to 'root'@'%' identified by 'root';
```
### denide for user (bash에서 설정)
```shell
chmod 644 /etc/my.cnf
```
### python 내 모듈 에러 ex)not found shortuuid
> 터미널에서 직접 들어가 재설치
```bash
docker ps
docker exec -it 52af9689a913 bash
cd /
cd usr/local/lib/python3.9/site-packages
pip install pyjwt
pip install shortuuid
```