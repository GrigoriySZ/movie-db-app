from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class CastMember(BaseModel):
    id: int = Field(..., description='ID актера')
    name: str = Field(..., min_length=1, max_length=50, description='Имя актера')
    character: str = Field(..., min_length=1, max_length=50, description='Имя персонажа')
    profile_path: Optional[str] = None

class MovieShort(BaseModel):
    id: int = Field(..., ge=0, description='ID фильма')
    title: str = Field(..., min_length=1, description='Название фильма')
    poster_path: Optional[str] = None
    release_date: Optional[datetime] = None
    vote_avarage: float = Field(..., ge=0, description='Средняя оценка фильма')

class MovieDetail(MovieShort):
    overview: str = Field(..., description='Описание фильма')
    cast: List[CastMember] = []