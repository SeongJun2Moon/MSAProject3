import '../styles/Login.css'
import { useState } from "react"
import { userLoginApi } from '../api'
import { useNavigate } from 'react-router-dom'

export default function LoginForm() {
    const [inputs, setInputs] = useState({})
    const {email, password} = inputs;
    const navigate = useNavigate()

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target 
        setInputs({...inputs, [name]: value})
    }
    
    const onClick = e => {
        e.preventDefault()
        const loginRequest = {email, password}
        alert(`사용자 이름: ${JSON.stringify(loginRequest)}`)
        userLoginApi(loginRequest)
        .then((res)=>{
            localStorage.setItem("loginUser", JSON.stringify(res.data))
            alert(`사용자 이름: ${localStorage.getItem("loginUser")}`)
            navigate("/home")
        })
        .catch((err)=>{
            console.log(err)
            alert('이메일 확인')
        })
    }

    return (
        <>
            EMAIL: <input type="text" name="email" onChange={onChange} /><br/>
            PASSWORD: <input type="text" name="password" onChange={onChange} /><br/>
            <button onClick={onClick}> 로그인 </button>
        </>
    )}