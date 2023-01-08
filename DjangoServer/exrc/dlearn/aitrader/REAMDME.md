# 에러
### Input 0 of layer "sequential" is incompatible with the layer : 차원 변경 에러
```python
x_train = x_train.astype(np.float32).reshape(x_train.shape[0], x_train[1], 1)
```

### ValueError: Failed to convert a NumPy array to a Tensor (Unsupported object type int) : 데이터 타입 에러
```python
y_train.astype(np.float32)
```

# 문법
### if "M" in df2.iloc[i, j]
> df.iloc = 인덱스 순서로 검색 ex) df.iloc[3] => 4번째 로우 출력 <-> df.loc = 인덱스 값으로 검색 ex) df.loc['a'] => 인덱스가 a 인 로우 출력
### df1 = df1.sort_values(['날짜'], ascending=[True])
> 오름차순 정리 : 날짜=기준칼럼, ascending=오름차순여부
### df1 = df1.values
> 데이터만 출력 => 넘파이파일로 바꾸기 전 형태만 갖추는 작업
```shell
# 그냥출력
                  종가      오픈      고가      저가          거래량
날짜                                                       
2022- 12- 02  315.02  320.76  320.76  315.02  114750000.0
2022- 12- 05  313.91  316.26  317.07  312.92  113970000.0

# value 출력
[[315.02 320.76 320.76 315.02 114750000.0]
 [313.91 316.26 317.07 312.92 113970000.0]]
```
### df.rename(columns={'오픈': '시가'}, inplace=True)
> 칼럼 이름 바꿔줌
### x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3, shuffle=False)
> train_teset_split = numpy 데이터의 로우를 train, test로 분할할 때 사용하는 사이킷런 메소드
> random_state = 난수 초기값 설정 => 암거나 주면 됨
> shuffle = train, test 분할 시 무작위로 섞을지 말지 여부 설정. 시계열 예측 같은 순서가 중요한 분류에선 필수
### scaler = StandardScaler()
> 스케일링(포준화, 정규화) 중 표준화 해주는 사이킷런 메소드
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(x_train)
x_train_scaled = scaler.transform(x_train).astype(float)
x_test_scaled = scaler.transform(x_test).astype(float)
```
> #### 메소드 설명
> - StandardScaler.fit() : 평균 𝜇과 표준편차 𝜎를 계산
> 
> - StandardScaler.transform() : 정규화/표준화, Standardization, z = (𝑥-𝜇)/𝜎
>
> - StandardScaler.fit_trasform() : fit() + transform()

> #### 프로세스
> 1. traning data 의 fit 을 한 후 → 분포를 객체에 저장
> 
> 2. traning data 의 transform 를 하고, 
>
> 3. test data 는  trasform 만 진행합니다.→ fit 된 분포를 그대로 적용

## model
### model = Sequential()
>학습모델 설정, 모델 학습 시에 다양한 메소드를 필수적으로 넣어줘야한다

### model.add
>계층설정, input_shape:데이터모양설정, activation:활성화함수 설정
```python
model.add(Dense(64, input_shape=(25,)))
model.add(Dense(32, activation='relu'))
```
### model.compile
>컴파일 : 모델학습 전 학습과정 설정
```python
model.compile(loss='mse', optimizer='adam', metrics=['mse'])
```
### model.fit
>학습
```python
model.fit(x_train_scaled, y_train, validation_split=0.2, verbose=1, batch_size=1, epochs=100,
                  callbacks=[early_stopping])
```
### model.evaluate
>평가
```python
loss, mse = model.evaluate(x_test_scaled, y_test, batch_size=1)
```
### model.predict
>예측값
```python
y_pred = model.predict(x_test_scaled)
```