from pydantic import BaseModel, EmailStr
from pydantic.types import constr

from settings import settings


class BaseUser(BaseModel):
    email: EmailStr
    username: str = constr(
        min_length=settings.username_min_len,
        max_length=settings.username_max_len,
    )


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class UserCreate(BaseUser):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
