import { PayloadAction } from "@reduxjs/toolkit";
import {call, delay, put, takeLatest} from 'redux-saga/effects'
import {string} from 'yup'
import userActions from '@/modules/users'
import { currentTime } from "@/components/admin/utils";
import { userJoinApi } from "@/apis/userApi";

//api


interface UserJoinType {
    type: string,
    payload : {
        user_email: string, user_name: string, password: string 
    }
}

interface UserJoinSuccessType {
    type: string,
    payload : {
        user_name: string 
    }
}

function* join(user: UserJoinType) {
    try{
        console.log(`${currentTime} : userSage 내부에서 패스트api로 넘기는 값: ${JSON.stringify(user)}`)
        // 오류시 userJoinApi 동일이름 경로 확인
        
        // const response : UserJoinSuccessType = yield userJoinApi(user.payload)
        // console.log(`${currentTime} : userSage 내부에서 join 성공: ${JSON.stringify(response)}`)
    }catch(error){
        console.log("userSaga 내부에서 join 안돼유")
    }
}

export function* watchJoin() {
    yield takeLatest(userActions.actions.joinRequest, join)
}