from typing import List

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class Article(BaseModel):
    user_id: UUID
    user_email: str
    password: str
    user_name: str
    phone: str
    create_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

