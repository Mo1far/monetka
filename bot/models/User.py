from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from bot.models.Wallet import Wallet
from bot.models.Transfer import Transfer
from bot.models.Game import Game
from bot.models.Transaction import Transaction

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    telegram_id = Column(Integer, primary_key=True, nullable= False, unique=True)
    username = Column(String(20), unique=True, nullable= False)

    wallets = relationship("Wallet", order_by=Wallet.telegram_id, back_populates="user")
    transfers = relationship("Transfer", order_by=Transfer.telegram_id, back_populates="user")
    transactions = relationship("Transaction", order_by=Transaction.telegram_id, back_populates="user")
    games = relationship("Game", order_by=Game.telegram_id, back_populates="user")

    def __self__(self, telegram_id, username):
        self.telegram_id = telegram_id
        self.username = username