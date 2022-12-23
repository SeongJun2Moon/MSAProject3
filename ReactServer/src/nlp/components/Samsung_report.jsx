import { useState } from "react";
import samsungService from "../api";
const Samsung = () => {
  const [words, setWords] = useState();

  const onClick = (e) => {
    e.preventDefault();
    samsungService.samsungWords().then((res) => {
      const json = JSON.parse(res); // JSON.parse : json을 js객체로 바꿈 =>.이나 []로 내부 데이터 접근 가능 <-> JSON.stringify()
      setWords(json["result"]);
      console.log(json);
      alert(words)
    });
    let arr = document.getElementsByClassName("box");
    for (let i = 0; i < arr.length; i++) arr[i].value = "";
  };

  return (
    <>
      <h2>삼성 리포트</h2>
      <button onClick={onClick}>단어 출력</button><br/>
      
    </>
  );
};
export default Samsung;
