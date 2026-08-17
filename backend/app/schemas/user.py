from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
    username: str = Field(..., min_length=1, max_length=50, description='Имя или никнейм пользователя')
    email: EmailStr = Field(..., description='Электронная почта пользователя')
    password: str = Field(..., min_length=1, max_length=50, description='Пароль от личного кабинета пользователя')

class userLogin(BaseModel):
    username: str = Field(..., min_length=1, max_length=50, description='Имя или никнейм пользователя')
    password: str = Field(..., min_length=1, max_length=50, description='Пароль от личного кабинета пользователя')

class userRead(BaseModel):
    id: int 
    username: str 
    email: EmailStr 
    created_at: datetime 

    model_config = ConfigDict(from_attributes=True)