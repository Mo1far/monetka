from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from .base import Base


class Wallet(Base):
    __tablename__ = 'wallet'

    id = Column(Integer, primary_key=True, nullable= False, unique=True, autoincrement=True)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'), nullable= False)
    adress = Column(String(60), nullable=False)
    balance =Column(Numeric(19, 7), nullable=False)


    def __init__(self, telegram_id, adress, balance):
        self.telegram_id = telegram_id
        self.adress = adress
        self.balance = balance

user = relationship("User", backref="wallets")
