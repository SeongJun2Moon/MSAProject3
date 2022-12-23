import "../styles/SignUp.css";

const SignUp = () => {
  const onClick = (e) => {
    e.preventDefault();
    return;
  };

  return (
    <>
      <h2>회원가입</h2>
      <button onClick={onClick}> 회원가입 </button>
      <br />
      <p>100명 등록해버리기</p>
      {}
    </>
  );
};

export default SignUp;

// const [inputs, setInputs] = useState({})
// const {email, password, nickname} = inputs;

// const onChange = e => {
//     e.preventDefault()
//     const {value, name} = e.target
//     setInputs({...inputs, [name]: value})
// }

// const onClick = e => {
//     e.preventDefault()
//     const loginRequest = {email, password, nickname}
//     alert(`사용자 이름: ${JSON.stringify(loginRequest)}`)
//     userLoginApi(loginRequest)
//     .then((res)=>{
//         console.log(`Response is ${res}`)
//         localStorage.setItem('token', JSON.stringify(res.config.data))
//     })
//     .catch((err)=>{
//         console.log(err)
//         alert('아이디와 비밀번호를 다시 입력해주세요')
//     })

// }EMAIL: <input type="text" name="email" onChange={onChange} /><br/>
// PASSWORD: <input type="text" name="password" onChange={onChange} /><br/>
// NICKNAME: <input type="text" name="nickname" onChange={onChange} /><br/>
