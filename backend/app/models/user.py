from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.session import Base
from datetime import datetime

from watchlist import Watchlist
from review import Review

class User(Base):
    __tablenames__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    watchlist: Mapped['Watchlist'] = relationship('Watchlist', back_populates='user', cascade='all, delete-orphan')
    reviews: Mapped[list['Review']] = relationship('Review', back_populates='user', cascade='all, delete-orphan')