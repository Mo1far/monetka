from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric

Base = declarative_base()

class Transactions(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, nullable= False, unique=True)
    telegram_id = Column(Integer, primary_key=True, nullable=False)
    token = Column(String(), primary_key=True, nullable=False)
    wallet_id = Column(Integer, primary_key=True, nullable=False)
    balance =Column(Numeric(19, 5), nullable=False)
    adress = Column(String(50), nullable=False)
