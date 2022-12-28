import { useState } from "react";
import webcrawlerService from "../api";
const NaverGrade = () => {
  const [inputs, setInputs] = useState({})
  const [grade, setgrade] = useState();
  
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
      setgrade(res);
      console.log(res);
    });
  };

  return (
    <>
      <h2>네이버 영화 선호여부</h2>
      확인할 리뷰 : <input onChange={onChange} type="text" name="inputs" />
      <button onClick={onClick}>Click</button>
      <p>버튼을 클릭하시면, 네이버영화 긍정률이 출력됩니다.</p>
      <table>
        <thead>
            <tr>
                <th>긍정도</th>
            </tr>
        </thead>
        <tbody>
        {positive && 
            <tr ><td>{Math.floor(positive*100, 3)} %</td></tr>
        }    
        </tbody>
    </table>
    </>
  );
};
export default NaverGrade;
