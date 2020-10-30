from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from .base import Base

class Token(Base):
    __tablename__ = 'tokens'

    token = Column(String(), primary_key=True, unique=True, nullable= False)
    wallet_id = Column(Integer, ForeignKey('wallet.id'), primary_key=True, nullable=False)
    ticker = Column(String(5), nullable=False)
    token_type = Column(String(10), nullable=False)
    balance =Column(Numeric(19, 7), nullable=False)

    def __init__(self, token, wallet_id, ticker, token_type, balance):
        self.token = token
        self.wallet_id = wallet_id
        self.ticker = ticker
        self.token_type = token_type
        self.balance = balance

wallet = relationship("Wallet", backref="tokens")