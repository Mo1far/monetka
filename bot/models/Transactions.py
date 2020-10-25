from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    telegram_id = Column(Integer, primary_key=True, nullable= False, unique=True)
    username = Column(String(20), unique=True, nullable= False)
    balance =Column(Numeric(10, 5), nullable=False)