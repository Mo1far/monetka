from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from .base import Base

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, nullable= False, unique=True, autoincrement=True)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'), primary_key=True, nullable=False)
    token = Column(String(), ForeignKey('tokens.token'), primary_key=True, nullable=False)
    wallet_id = Column(Integer, ForeignKey('tokens.wallet_id'), primary_key=True, nullable=False)
    balance =Column(Numeric(19, 7), nullable=False)
    adress = Column(String(60), nullable=False)
    hash=Column(String(60), nullable=False)

    def __init__(self, telegram_id, token, wallet_id, balance, adress, hash):
        self.telegram_id = telegram_id
        self.token = token
        self.wallet_id = wallet_id
        self.balance = balance
        self.adress = adress
        self.hash = hash


user = relationship("User", backref="transactions")
tokens = relationship("Token", backref="transactions")