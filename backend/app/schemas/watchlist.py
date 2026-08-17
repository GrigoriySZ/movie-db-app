from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class WatchlistCreate(BaseModel): 
    tmdb_movie_id: int = Field(..., ge=0, description='ID фидбма в базе TMDB')

class WatchlistRead(BaseModel): 
    id: int
    tmdb_movie_id: int
    user_id: int 
    added_at: datetime

    model_config = ConfigDict(from_attributes=True)
