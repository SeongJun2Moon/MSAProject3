from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi import APIRouter
import app.repositories.post as dao
from ..database import get_db
router = APIRouter()

@router.get("/")
async def get_posts(db: Session = Depends(get_db)):
    return {"data": dao.find_posts(db=db)}