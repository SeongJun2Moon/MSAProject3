from typing import List
from typing import Optional

from pydantic import BaseModel
from uuid import UUID

class ArticleDTO(BaseModel):
    art_seq: Optional[int]
    title: Optional[str]
    content: Optional[str]
    created: Optional[str]
    modified: Optional[str]
    user_id: Optional[str]

    class Config:
        orm_mode = True

