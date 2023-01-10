from typing import List

from pydantic import BaseModel

class Post(BaseModel):
    user_id: int
    user_email: str
    password: str
    user_name: str
    phone: str

    class Config:
        orm_mode = True

