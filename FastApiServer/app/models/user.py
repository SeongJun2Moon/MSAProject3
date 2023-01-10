from pydantic import BaseModel as base, BaseConfig
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from ..database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_email = Column(String(20), nullable=False) # django의 model 역할
    password = Column(String(20), nullable=False) # nullable:필수작성 공란안됨
    user_name = Column(String(20), nullable=False)
    phone = Column(String(20))
    birth = Column(String(20))
    address = Column(String(20))
    job = Column(String(20))
    user_interests = Column(String(20))
    token = Column(String(20))

    class Config:
        BaseConfig.arbitrary_types_allowed = True
        allow_population_by_field_name = True