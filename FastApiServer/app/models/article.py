from pydantic import BaseConfig
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import  relationship
from app.database import Base
from sqlalchemy_utils import UUIDType

class Article(Base):

    __tablename__ = 'articles'

    art_seq = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(20), nullable=False)
    content = Column(String(20), nullable=False)
    user_id = Column(UUIDType(binary=False), ForeignKey('users.user_id'))


    user = relationship('User', back_populates='articles')


    class Config:
        BaseConfig.arbitrary_types_allowed = True
        allow_population_by_field_name = True