import { ChangeEvent,FormEvent, useState } from "react"
import { NextPage } from "next"
import { Login,  GoogleLogin} from "@/src/components/user"
import { User } from "@/src/modules/types"
import { useDispatch } from "react-redux"
import { loginRequest } from "@/src/modules/slices"

const LoginPage: NextPage = function(){
    const [loginInfo, setLoginInfo] = useState<User>({user_email:'', password:''})
    const dispatch = useDispatch()

    // user_email : string,
    // password : string,

    const onChange = (e: ChangeEvent<HTMLInputElement>) => {
        e.preventDefault()
        const { name, value} = e.currentTarget
        setLoginInfo({...loginInfo, [name]:value})
    }
    const onSubmit = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault()
        dispatch(loginRequest(loginInfo))
    }
    return (
        <>
           <Login onChange={onChange} onSubmit={onSubmit}/>
           <GoogleLogin/>
        </>
            
        
 );
}
LoginPage.getInitialProps =async (ctx) => {
    const pathname = ctx.pathname
    return { pathname }
}
export default LoginPage