from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class ReviewCreate(BaseModel):
    tmdb_movie_id: int = Field(..., ge=0, description='ID фильма в базе TMDB')
    reting: int = Field(..., ge=1, le=10, description='Оценка фильма обзорщика')
    content: str = Field(..., description='Содержание обзора')
    author_username: str = Field(..., min_length=1, max_length=50, description='Имя автора обзора')

class ReviewRead(BaseModel):
    id: int 
    tmdb_movie_id: int
    reting: int 
    content: str 
    author_username: str 
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)