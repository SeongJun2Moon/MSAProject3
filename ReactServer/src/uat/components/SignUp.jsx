import { useState } from "react";
import { randomUserMaker } from "../api";
const SignUp = () => {
  const [user, setUser] = useState();

  const onClick = (e) => {
    e.preventDefault();
    randomUserMaker.randomUsers().then((res) => {
      const json = JSON.parse(res); // JSON.parse : json을 js객체로 바꿈 =>.이나 []로 내부 데이터 접근 가능 <-> JSON.stringify()
      setUser(json["result"]);
      console.log(json["result"]);
      alert("소환");
    });
  };

  return (
    <>
      <h2>회원가입</h2>
      <button onClick={onClick}>100명 소환</button>
      <p>버튼을 클릭하시면, 랜덤한 100명이 나와버립니다.</p>
      {
        <table>
          <th>ID</th>
          <th>이메일</th>
          <th>비밀번호</th>
          <th>이름</th>
          <th>휴대폰번호</th>
          <th>생일</th>
          <th>주소</th>
          <th>직업</th>
          <th>취미</th>
          <th>토큰</th>
          {user &&
            user.map(
              ({
                id,
                user_email,
                password,
                user_name,
                phone,
                birth,
                address,
                job,
                user_interests,
                token,
              }) => (
                <tr key={id}>
                  <td>{id}</td>
                  <td>{user_email}</td>
                  <td>{password}</td>
                  <td>{user_name}</td>
                  <td>{phone}</td>
                  <td>{birth}</td>
                  <td>{address}</td>
                  <td>{job}</td>
                  <td>{user_interests}</td>
                  <td>{token}</td>
                </tr>
              )
            )}
        </table>
      }
    </>
  );
};
export default SignUp;
