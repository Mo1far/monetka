from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy import ForeignKey

Base = declarative_base()

class Transfer(Base):
    __tablename__ = 'transfer'

    id = Column(Integer, primary_key=True, nullable= False, unique=True)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'), primary_key=True, nullable= False)
    hash = Column(String(60), nullable=False, unique=True)
    balance =Column(Numeric(19, 7), nullable=False)
    id_destination = Column(Integer, nullable= False)



