from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, SMALLINT
from sqlalchemy import ForeignKey

Base = declarative_base()

class Rounds_info(Base):
    __tablename__ = 'rounds_info'

    round_id = Column(Integer, primary_key=True, nullable=False, unique=True)
    games_id = Column(Integer, ForeignKey('games.id'), primary_key=True, nullable=False)
    creator_telegram_id = Column(Integer, ForeignKey('games.telegram_id'), primary_key=True, nullable=False)
    color_victory = Column(String(5),nullable=False)
    block_num = Column(SMALLINT, nullable=False)
    block_height = Column(String(60), nullable=False)
    balance = Column(Numeric(19, 7), nullable=False)
    vinner_telegram_id = Column(Integer, nullable=False)