from sqlalchemy import Column, Integer, String, Numeric, SMALLINT
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from .base import Base

class Round_info(Base):
    __tablename__ = 'rounds_info'

    round_id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    games_id = Column(Integer, ForeignKey('games.id'), primary_key=True, nullable=False)
    telegram_id = Column(Integer, ForeignKey('games.telegram_id'), primary_key=True, nullable=False)
    color_victory = Column(String(5), nullable=False)
    block_num = Column(SMALLINT, nullable=False)
    block_height = Column(String(60), nullable=False)
    balance = Column(Numeric(19, 7), nullable=False)
    vinner_id = Column(Integer, nullable=False)


    def __init__(self, round_id, games_id, creator_telegram_id, color_victory, block_num, block_heigth,
                 balance, vinner_id):
        self.round_id = round_id
        self.games_id = games_id
        self.creator_telegram_id = creator_telegram_id
        self.color_victory = color_victory
        self.block_num = block_num
        self.block_height = block_heigth
        self.balance = balance
        self.vinner_id = vinner_id

game = relationship("Game", backref="rounds")