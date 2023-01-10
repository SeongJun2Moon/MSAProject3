from uuid import uuid4
from pydantic import BaseConfig
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import UUIDType
from sqlalchemy.orm import relationship

from ..database import Base

class User(Base):
    __tablename__ = 'users'
    user_id = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    user_email = Column(String(20), nullable=False) # django의 model 역할
    password = Column(String(20), nullable=False) # nullable:필수작성 공란안됨
    user_name = Column(String(20), nullable=False)
    phone = Column(String(20))
    birth = Column(String(20))
    address = Column(String(20))
    job = Column(String(20))
    user_interests = Column(String(20))
    token = Column(String(20))
    # create_at = Column(String(30))
    # update_at = Column(String(30))

    articles = relationship('Articles', back_populates='user')

    class Config:
        BaseConfig.arbitrary_types_allowed = True
        allow_population_by_field_name = True