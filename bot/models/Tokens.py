from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

Base = declarative_base()

class Users(Base):
    __tablename__ = 'tokens'

    token = Column(String(), primary_key=True, unique=True, nullable= False)
    wallet_id = Column(Integer, ForeignKey('wallet.id'), primary_key=True, nullable=False)
    ticker = Column(Integer(5), nullable=False)
    token_type = Column(Integer(5), nullable=False)