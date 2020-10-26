from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric

Base = declarative_base()

class Users(Base):
    __tablename__ = 'wallet'

    id = Column(Integer, primary_key=True, nullable= False, unique=True)
    telegram_id = Column(Integer, nullable= False, unique=True)
    adress = Column(String(255), nullable=False)