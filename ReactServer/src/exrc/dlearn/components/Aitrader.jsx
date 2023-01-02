import { useState } from "react";
import { webcrawlerService } from "../api";
const AiTraders = () => {
  const [traders, setTraders] = useState();

  const onClick = (e) => {
    e.preventDefault();

    webcrawlerService.samsungtraders().then((res) => {
      const json = JSON.parse(res); // JSON.parse : json을 js객체로 바꿈 =>.이나 []로 내부 데이터 접근 가능 <-> JSON.stringify()
      setTraders(json["result"]);
      console.log(json["result"]);
    });
  };

  return (
    <>
      <h2>삼성주가</h2>
      <button onClick={onClick}>Click</button>
      <p>버튼을 클릭하시면, 삼성주가가 출력됩니다.</p>
      {/* {
        <table>
          <th>종가</th>
          <th>예측가</th>
          {traders &&
            traders.map(({ 종가, 예측가 }) => (
              <tr key={종가}>
                <td>{종가}</td>
                <td>{예측가}</td>
              </tr>
            ))}
        </table>
      } */}
    </>
  );
};
export default AiTraders;
