from typing import List

from pydantic import BaseModel

class User(BaseModel):
    user_id : int
    user_email : str
    password : str
    user_name : str
    phone : str
    birth : str
    address : str
    job : str
    user_interests : str
    token : str

    class Config:
        orm_mode = True

class UserList(User):
    users: List[User] = []

class Post(BaseModel):
    posts_id : int
    title : str
    content : str
    created_at : str
    updated_at : str

    class Config:
        orm_mode = True

class PostList(User):
    posts: List[Post] = []