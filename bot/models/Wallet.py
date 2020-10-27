from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey


Base = declarative_base()

class Users(Base):
    __tablename__ = 'wallet'

    id = Column(Integer, primary_key=True, nullable= False, unique=True)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'), nullable= False, unique=True)
    adress = Column(String(60), nullable=False)