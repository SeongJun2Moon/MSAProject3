from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.repositories.user import find_users, find_posts
from app.database import get_db


user_router = APIRouter()
post_router = APIRouter()


@user_router.get('/', tags=["users"])
async def get_users(db : Session = Depends(get_db)):
    return {"data" : find_users(db=db)}


@post_router.get('/', tags=["posts"])
async def get_posts(db : Session = Depends(get_db)):
    return {"data" : find_posts(db=db)}
