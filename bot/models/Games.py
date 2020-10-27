from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

Base = declarative_base()

class Games(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'), primary_key=True, nullable=False)
    token_type = Column(String(10), nullable=False)
