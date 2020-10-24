from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, SMALLINT

Base = declarative_base()

class Rounds_info(Base):
    __tablename__ = 'users_info'

    round_id = Column(Integer, primary_key=True, nullable= False, unique=True)
    games_id = Column(Integer, primary_key=True, nullable= False, unique=True)
    creator_telegram_id = Column(Integer, primary_key=True, nullable= False, unique=True)
    color_wictory = Column(String(5),nullable= False)
    block_num = Column(SMALLINT, nullable=False)
    block_height = Column(String,nullable= False)
    balance = Column(Numeric(19, 5), nullable=False)
    winner_telegram_id = Column(Integer, nullable=False)