from sqlalchemy import Column, Integer, String
from .base import Base


class User(Base):
    __tablename__ = 'users'

    telegram_id = Column(Integer, primary_key=True, nullable= False, unique=True)
    username = Column(String(20), unique=True, nullable= False)

    def __self__(self, telegram_id, username):
        self.telegram_id = telegram_id
        self.username = username




