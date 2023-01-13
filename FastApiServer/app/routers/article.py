from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import app.repositories.article as dao
from app.database import get_db


router = APIRouter()


@router.get('/{page}')
async def get_article(page: int, db: Session = Depends(get_db)):
    ls = dao.find_articles(page, db)
    return {'data': ls}