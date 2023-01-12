import axios, { AxiosResponse } from "axios"
import { context } from "@/components/admin/enum"

export interface UserType {
    user_id : string
    user_email : string
    password : string
    user_name : string
    phone : string
    birth : string
    address : string
    job : string
    user_interests : string
    token : string
    create_at : string
    updated_at : string  
}

export const userJoinApi = async (
                                payload:{
                                user_email : string,
                                password : string,
                                user_name : string,
                                phone : string,
                                birth : string,
                                address : string,
                                job : string,
                                user_interests : string
                                    }) => {
    const headers = context.headers
    try{
        const response :  AxiosResponse<unknown, UserType[]> = await axios.post(`${context.SERVER}`, payload, {headers})
    } catch(err) {

    }
}