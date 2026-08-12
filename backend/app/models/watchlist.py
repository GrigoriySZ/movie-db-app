from sqlalchemy import Integer,  ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.session import Base
from datetime import datetime

from user import User

class Watchlist(Base):
    __tablename__ = 'watchlist'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    tmdb_movie_id: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    added_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    user: Mapped['User'] = relationship('User', back_populates='watchlist')