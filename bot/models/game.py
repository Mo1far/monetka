from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from .base import Base

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'), primary_key=True, nullable=False)
    token_type = Column(String(10), nullable=False)


    def __init__(self, telegram_id, token_type):
        self.telegram_id = telegram_id
        self.token_type = token_type


user = relationship("User", backref="games")