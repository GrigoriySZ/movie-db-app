from sqlalchemy import Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.session import Base
from datetime import datetime

from user import User

class Review(Base):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    tmdb_movie_id: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    ratind: Mapped[int] = mapped_column(Integer, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    user: Mapped['User'] = relationship('User', back_populates='')
