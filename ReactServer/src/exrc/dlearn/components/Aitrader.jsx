import { useState } from "react";
import { AitGet } from "../api";
const AiTraders = () => {
  const [traders, setTraders] = useState();
  const [inputs, setInputs] = useState({});

  const onChange = (e) => {
    e.preventDefault();
    const { value, name } = e.target;
    setInputs({ ...inputs, [name]: value });
  };

  const onClick = (e) => {
    e.preventDefault();
    AitGet(inputs["string"]).then((res) => {
      const json = JSON.parse(res); // JSON.parse : json을 js객체로 바꿈 =>.이나 []로 내부 데이터 접근 가능 <-> JSON.stringify()
      setTraders(json["result"]);
      alert(json["result"]);
    });
  };

  return (
    <>
      <h2>언어 측정률</h2>
      <form>
        DNN : <input type="date" name="string" onChange={onChange} />
        <button onClick={onClick}>DNN 주가 예측</button>
      </form>
      <br />
      <form>
        DNN_Ensemble : <input type="date" name="string" onChange={onChange} />
        <button onClick={onClick}>주가 예측</button>
      </form>
      <br />
      <form>
        LSTM : <input type="date" name="string" onChange={onChange} />
        <button onClick={onClick}>주가 예측</button>
      </form>
      <br />
      <form>
        LSTM_Ensemble : <input type="date" name="string" onChange={onChange} />
        <button onClick={onClick}>주가 예측</button>
      </form>
      <br />
      <table>
        <thead>
          <tr>
            <th>주가 예측 </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{traders}</td>
          </tr>
        </tbody>
      </table>
    </>
  );
};
export default AiTraders;
