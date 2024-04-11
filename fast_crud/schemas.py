from pydantic import BaseModel
from typing import Optional


class Users(BaseModel):
    email: str
    username: str
    password:str
    is_active:Optional[bool] = True

    class Config:
        orm_mode = True


class login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class Usershow(BaseModel):
    id:int
    email: str
    username: str
    is_active:bool

    class Config:
        orm_mode = True


class Students(BaseModel):
    user_id:int
    roll: int
    name: str
    marks:float

    class Config:
        orm_mode = True
