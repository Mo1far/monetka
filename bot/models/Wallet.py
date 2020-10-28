from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from bot.models.Token import Token


Base = declarative_base()

class Wallet(Base):
    __tablename__ = 'wallet'

    id = Column(Integer, primary_key=True, nullable= False, unique=True, autoincrement=True)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'), nullable= False)
    adress = Column(String(60), nullable=False)
    balance =Column(Numeric(19, 7), nullable=False)

    user = relationship('User', back_populates='wallets')

    tokens = relationship('Token', order_by=Token.wallet_id, back_populates='wallet')

    def __init__(self, telegram_id, adress, balance):
        self.telegram_id = telegram_id
        self.adress = adress
        self.balance = balance