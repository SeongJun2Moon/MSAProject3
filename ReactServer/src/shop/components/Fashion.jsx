import { ApiPost, ApiGet } from "../api";
import { useState } from "react";

const Fashion = () => {
  const [inputs, setInputs] = useState({});
  const { id1, id2 } = inputs;

  const onChange = (e) => {
    e.preventDefault();
    const { value, name } = e.target;
    setInputs({ ...inputs, [name]: value });
  };

  const onClick_get = (e) => {
    e.preventDefault();
    alert(`리퀘스트 데이터: ${JSON.stringify(id1)}`);
    ApiGet(id1)
      .then((res) => {
        alert(`찾는 옷 : ${JSON.stringify(res.data.result)}`);
      })
      .catch((err) => {
        console.log(err);
        alert("땡");
      });
  };

  const onClick_post = (e) => {
    const request = { id2 };
    e.preventDefault();
    alert(`리퀘스트 데이터: ${JSON.stringify(request)}`);
    ApiPost(request)
      .then((res) => {
        alert(`찾는 옷 : ${JSON.stringify(res.data.result)}`);
      })
      .catch((err) => {
        console.log(err);
        alert("땡");
      });
  };

  return (
    <>
      옷은 1부터 20까지 : <input type="text" name="id1" onChange={onChange} />
      <br />
      <button onClick={onClick_get}> GET </button>
      <br />
      옷은 1부터 20까지 : <input type="text" name="id2" onChange={onChange} />
      <br />
      <button onClick={onClick_post}> POST </button>
    </>
  );
};

export default Fashion;
