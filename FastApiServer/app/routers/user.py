from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.repositories.user import find_users
from app.database import get_db


router = APIRouter()

@router.get('/')
async def get_users(db : Session = Depends(get_db)):
    return {"data" : find_users(db=db)}

@router.post('/')
async def join(user: User, db:Session = Depends(get_db)):
    user_dict = user.dict()

    return {"data" : signup(db=db)}

@router.post('/login/{id}')
async def login(db : Session = Depends(get_db)):
    return {"data" : login(db=db)}

@router.put('/{id}')
async def update(id:str, user:User, db:Session = Depends(get_db)):
    return {"data" : "success"}

@router.put('/{id}')
async def delete(id:str, user:User, db:Session = Depends(get_db)):
    return {"data" : "success"}

@router.get('/page/{no}')
async def get_users(db : Session = Depends(get_db)):
    return {"data" : find_users(db=db)}

@router.get('/email/{no}')
async def get_users(db : Session = Depends(get_db)):
    return {"data" : find_users(db=db)}