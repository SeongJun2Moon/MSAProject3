from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi import APIRouter
from app.repositories.post import find_posts
from ..database import get_db

router = APIRouter()

@router.get("/")
async def get_posts(db: Session = Depends(get_db)):
    return {"data": find_posts(db=db)}
