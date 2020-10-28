from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from bot.models.Transaction import Transaction

Base = declarative_base()

class Token(Base):
    __tablename__ = 'tokens'

    token = Column(String(), primary_key=True, unique=True, nullable= False)
    wallet_id = Column(Integer, ForeignKey('wallet.id'), primary_key=True, nullable=False)
    ticker = Column(Integer(5), nullable=False)
    token_type = Column(Integer(5), nullable=False)
    balance =Column(Numeric(19, 7), nullable=False)

    wallet = relationship("Wallet", back_populates='tokens')

    transactions_token = relationship("Transaction", order_by=Transaction.token, back_populates="token_token")
    transactions_wallet_id = relationship("Transaction", order_by=Transaction.token, back_populates="token_wallet_id")


    def __init__(self, token, wallet_id, ticker, token_type, balance):
        self.token = token
        self.wallet_id = wallet_id
        self.ticker = ticker
        self.token_type = token_type
        self.balance = balance
