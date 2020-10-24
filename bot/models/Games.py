from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Games(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    userstelegram_id = Column(Integer, primary_key=True, nullable=False)
    token_type = Column(String(10), nullable=False)