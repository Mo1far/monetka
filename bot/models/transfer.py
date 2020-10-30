from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from .base import Base

class Transfer(Base):
    __tablename__ = 'transfer'

    id = Column(Integer, primary_key=True, nullable= False, unique=True, autoincrement=True)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'), primary_key=True, nullable= False)
    hash = Column(String(60), nullable=False, unique=True)
    balance =Column(Numeric(19, 7), nullable=False)
    id_destination = Column(Integer, nullable= False)

    def __init__(self, telegram_id, hash, balance, id_destination):
        self.telegram_id = telegram_id
        self.hash = hash
        self.balance = balance
        self.id_destination = id_destination

user = relationship("User", backref="transfers")

