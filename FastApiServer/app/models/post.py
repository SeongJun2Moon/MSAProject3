from pydantic import BaseConfig
import datetime
from sqlalchemy import Column, Integer, String, DateTime
from ..database import Base


class Post(Base):
    __tablename__ = 'posts'
    posts_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    title = Column(String(20), nullable=False) # django의 model 역할
    content = Column(String(20), nullable=False) # nullable:필수작성 공란안됨
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    class Config:
        BaseConfig.arbitrary_types_allowed = True
        allow_population_by_field_name = True
