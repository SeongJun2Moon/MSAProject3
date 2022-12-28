import { irisApi } from "../api";
import { useState } from "react";

const Iris = () => {
  const [inputs, setInputs] = useState({});
  const { SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm } = inputs;

  const onChange = (e) => {
    e.preventDefault();
    const { value, name } = e.target;
    setInputs({ ...inputs, [name]: value });
  };

  const onClick = (e) => {
    e.preventDefault();
    const IrisRequests = {
      SepalLengthCm,
      SepalWidthCm,
      PetalLengthCm,
      PetalWidthCm,
    };
    alert(`사용자 이름: ${JSON.stringify(IrisRequests)}`);
    irisApi(IrisRequests)
      .then((res) => {
        console.log(`Response is ${res.config.data}`);
        localStorage.setItem("token", JSON.stringify(res.config.data));
        alert(`찾는 품종 : ${JSON.stringify(res.data.붓꽃품종)}`);
      })
      .catch((err) => {
        console.log(err);
        alert("땡");
      });
  };

  return (
    <>
      꽃잎 길이 : <input type="text" name="PetalLengthCm" onChange={onChange} />
      <br />
      꽃잎 폭: <input type="text" name="PetalWidthCm" onChange={onChange} />
      <br />
      꽃받침 길이:{" "}
      <input type="text" name="SepalLengthCm" onChange={onChange} />
      <br />
      꽃받침 폭: <input type="text" name="SepalWidthCm" onChange={onChange} />
      <br />
      <button onClick={onClick}> 실행 </button>
    </>
  );
};

export default Iris;
