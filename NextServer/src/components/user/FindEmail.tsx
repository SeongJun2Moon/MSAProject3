export default function FindEmail() {
    <>
    <>
        <h1>이메일 찾기</h1>
        <form action="/send-data-here" method="post">
            <label htmlFor='user_email'>Email:</label>
            <input minLength={4} maxLength={20} type="text" id="user_email" name="user_email" />
            <label htmlFor='password'>Password:</label>
            <input minLength={4} maxLength={20} type="text" id="password" name="password" />
            <button type="submit">Submit</button>
        </form>
        </>  
    </>
}