import axios, { AxiosResponse } from 'axios'
import { context } from '@/src/components/admin/enum'
import { currentTime } from '@/src/components/admin/utils'
import { User } from '@/src/modules/types'
import { author, client } from "@/src/modules/controllers"

export const user = {
    async join(payload: { 
        user_id? : string,
        user_email : string,
        password : string,
        user_name : string,
        phone? : string,
        birth? : string,
        address? : string,
        job? : string,
        user_interests? : string,
        token? : string,
        created_at? : string,
        updated_at? : string}){
            const url = `${context.server}/users/join`
            alert(`URL(api) is ${url}`)
            try{
                const response : AxiosResponse<unknown, User[]> = await axios.post(url)
                alert(` fastapi 다녀옴: ${JSON.stringify(response.data)} `)
                return response.data
            }catch(err){
                console.log(` ${currentTime} : userSaga 내부에서 join 실패 `)
            }
        },
    async login(payload: User){
        try{
            const response : AxiosResponse<any, User[]> =
            await author.post('/users/login', payload)
            return response.data
        }catch(err){
            return err;
        }
    },
    async logout(){
        try{
            await client.post('/users/logout')
        } catch(err){
            console.log(err)
            return err;
        }
    },
    async userInfo(){
        try{
            const response : AxiosResponse = await client.get(`/users/join`)
            return response.data
        } catch(err) {
            console.log(err)
            return err
        }
    }
    
}