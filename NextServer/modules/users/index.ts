import {createSlice, PayloadAction} from "@reduxjs/toolkit"
export interface IUserType {
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

export interface IUserState {
    data: IUserType[]
    status: 'idle'| 'loading' | 'failed'
} 

const initialState: IUserState = {
    data: [],
    status: 'idle',
}

const userSlice = createSlice({
    name: 'userSlice',
    initialState,
    reducers: {
        // const 함수 = () => {} 요거 숏컷 
        // 파라미터 <-> 페이로드 : 들어온 데이터 다 안쓰고 알짜베기만 씀
        // _payload -> _는 내부에서만 쓰는 보안데이터라는 뜻 => 베포할 때 오류 대비
        joinRequest(state: IUserState, _payload){
            state.status = 'loading'
        },
        joinSuccess(state: IUserState, {payload}){
            state.status = 'idle'
            state.data = [...state.data, payload]
        },
        joinFailed(state: IUserState, {payload}){
            state.status = 'failed'
            state.data = [...state.data, payload]
        },
        loginRequest(state: IUserState, _payload){
            state.status = 'loading'
        },
        loginSuccess(state: IUserState, {payload}){
            state.status = 'idle'
            state.data = [...state.data, payload]
        },
        loginFailed(state: IUserState, {payload}){
            state.status = 'failed'
            state.data = [...state.data, payload]
        },
    }
}
)

export const {
    joinRequest, joinSuccess, joinFailed,
    loginRequest, loginSuccess, loginFailed
} = userSlice.actions

export default userSlice