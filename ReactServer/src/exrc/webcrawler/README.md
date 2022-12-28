# 데이터호출법1 - Promise

### Promise 세팅

1. 백앤드 경로에서 response 가져오기

```javascript
async function naverMovie() {
  const res = await fetch(`${server}${webcrawler}`) //server:백호스트, webcrawler:백경로
    .then(handleResponse) // 오류정제 및 JSON->object
    .then((data) => JSON.stringify(data)) //JSON.stringify() : 딕셔너리를 JSON으로 변환
    .catch((error) => {
      alert("error :::: " + error);
    });
  return Promise.resolve(res);
}
```

2. 이벤트리스터로 데이터 호출하기

```javascript
const onClick = (e) => {
  e.preventDefault();
  webcrawlerService.naverMovie().then((res) => {
    const json = JSON.parse(res); // JSON.parse : json을 object로 바꿈 =>.이나 []로 내부 데이터 접근 가능 <-> JSON.stringify()
    setMovie(json["result"]);
    console.log(json);
  });
  let arr = document.getElementsByClassName("box");
  for (let i = 0; i < arr.length; i++) arr[i].value = "";
};
```

## 옵저버 패턴(pub/sub(발행/구독) 패턴)

### 옵저버 패턴이란

- 비동기를 구현하기 위한 패턴
- ...

### 프로미스란

- 자바스크립트 객체
-

## api/index.js

- async function : 비동기 함수 설정
- await fetch : ??
  - fetch는 ES6의 내장라이브러리
  - 프로미스 - axios와 fetch : ??

## NaverMovie.jsx

- JSON.parse : json을 js객체로 바꿈 =>.이나 []로 내부 데이터 접근 가능 <-> JSON.stringify()
