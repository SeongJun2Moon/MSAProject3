import { useState } from "react";
import webcrawlerService from "../api";

const KoreanClassify = () => {
  const [inputs, setInputs] = useState({});
  const { from, sentence } = inputs;
  const [korean, setKorean] = useState();

  const onChange = (e) => {
    e.preventDefault();
    const { value, name } = e.target;
    setInputs({ ...inputs, [name]: value });
  };

  const onClick = (e) => {
    e.preventDefault();
    const koreanRequest = { from, sentence };
    alert(`리뷰: ${JSON.stringify(koreanRequest)}`);
    webcrawlerService.koreanClassify(koreanRequest).then((res) => {
      const json = JSON.parse(res); // JSON.parse : json을 객체로 바꿈 =>.이나 []로 내부 데이터 접근 가능 <-> JSON.stringify()
      setKorean(json["result"]);
      console.log(json["result"]);
    });
  };

  return (
    <>
      <form method="post">
        <h2>문장의 국적이 어디입니까</h2>
        확인할 문장 : <input onChange={onChange} type="text" name="from" />
        <br />
        국적 조회 : <input onChange={onChange} type="text" name="sentence" />
        <br />
        <button onClick={onClick}>Click</button>
      </form>
      <table>
        <thead>
          <tr>
            <th>정답률</th>
          </tr>
        </thead>
        <tbody>
          {korean && (
            <tr>
              <td>{korean}</td>
            </tr>
          )}
        </tbody>
      </table>
    </>
  );
};
export default KoreanClassify;
