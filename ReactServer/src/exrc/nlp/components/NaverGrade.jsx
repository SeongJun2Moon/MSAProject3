import { useState } from "react";
import webcrawlerService from "../api";

const NaverGrade = () => {
  const [inputs, setInputs] = useState({})
  const [grade, setGrade] = useState();
  
  const onChange = e => {
    e.preventDefault()
    const {value, name} = e.target 
    setInputs({...inputs, [name]: value})
}

  const onClick = (e) => {
    e.preventDefault();
    alert(`리뷰: ${JSON.stringify(inputs)}`)
    webcrawlerService.navergrade(inputs)
    .then((res) => {
      const json = JSON.parse(res); // JSON.parse : json을 객체로 바꿈 =>.이나 []로 내부 데이터 접근 가능 <-> JSON.stringify()
      setGrade(json["result"]);
      console.log(json["result"]);
    });
  };

  return (
    <>
    <form method="post">
    <h2>네이버 영화 선호여부</h2>
      확인할 리뷰 : <input onChange={onChange} type="text" name="inputs" />
      <button onClick={onClick}>Click</button>
    </form>
      <table>
        <thead>
            <tr>
                <th>긍정도</th>
            </tr>
        </thead>
        <tbody>
        {grade && 
            <tr ><td>{Math.floor(grade, 3)} %</td></tr>
        }    
        </tbody>
    </table>
    </>
  );
};
export default NaverGrade;
