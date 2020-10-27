from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy import ForeignKey

Base = declarative_base()

class Transactions(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, nullable= False, unique=True)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'), primary_key=True, nullable=False)
    token = Column(String(), ForeignKey('tokens.token'), primary_key=True, nullable=False)
    wallet_id = Column(Integer, ForeignKey('tokens.wallet_id'), primary_key=True, nullable=False)
    balance =Column(Numeric(19, 7), nullable=False)
    adress = Column(String(60), nullable=False)
    hash=Column(String(60), nullable=False)
