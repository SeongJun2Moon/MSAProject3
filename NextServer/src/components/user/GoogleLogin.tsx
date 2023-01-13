import React, { useState, useRef } from 'react';


export default function GoogleLogin(){

    return (
        <>
        <h1>구글로그인</h1>
        <form action="/send-data-here" method="post">
            <label htmlFor='user_email'>Email:</label>
            <input required minLength={4} maxLength={20} type="text" id="user_email" name="user_email" />
            <label htmlFor='password'>Password:</label>
            <input required minLength={4} maxLength={20} type="text" id="password" name="password" />
            <button type="submit">Submit</button>
        </form>
        </>        
 );
}