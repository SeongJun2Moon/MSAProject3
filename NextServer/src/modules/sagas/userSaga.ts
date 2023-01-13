import { PayloadAction } from "@reduxjs/toolkit"
import { call, delay, put, takeLatest } from "redux-saga/effects"
import { joinRequest, joinSuccess,
    userAction } from '@/src/modules/slices';
import { User } from '@/src/modules/types';
import { user } from '@/src/modules/controllers';
// api 

export function* watchJoin(){
    alert(" %%% export function* watchJoin()")
    yield takeLatest(joinRequest, (action: {payload: User}) => {
        try{
            alert("3 saga joinRequest")
            const response: any = user.join(action.payload)
            console.log(' 진행 3: saga내부 join 성공  '+ JSON.stringify(action.payload))
            put(joinSuccess(response.payload))
            window.location.href = '/'
        }catch(error){
            put(userAction.joinFailure(error))
        }
    })
}

