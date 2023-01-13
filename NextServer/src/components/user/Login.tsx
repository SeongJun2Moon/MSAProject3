import React, { useState, useRef } from 'react';
import axios from "axios";


export default function Login(){
    // const [inputs, setInputs] = useState({})
    // const user_email = inputs;
    // const password = inputs;

    // const onChange = (e:any) => {
    //     e.preventDefault()
    //     const {value, name} = e.target 
    //     setInputs({...inputs, [name]: value})
    // }  

    // const onClick = (e:any) => {
    //     e.preventDefault()
    //     const loginRequest = {user_email, password}
    //     axios.post()
    // }

    return (
        <>
        <h1>로그인</h1>
        <form action="/send-data-here" method="post">
            <label htmlFor='user_email'>Email:</label>
            <input 
            // onChange={onChange}
             required minLength={4} maxLength={20} type="text" id="user_email" name="user_email" />
            <br/>
            <label htmlFor='password'>Password:</label>
            <input 
            // onChange={onChange} 
            required minLength={4} maxLength={20} type="text" id="password" name="password" />
            <br/>
            <button type="submit">Submit</button>
        </form>
        </>        
 );
}
