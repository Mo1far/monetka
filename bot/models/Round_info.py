from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, SMALLINT
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Round_info(Base):
    __tablename__ = 'rounds_info'

    round_id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    game_id = Column(Integer, ForeignKey('games.id'), primary_key=True, nullable=False)
    creator_telegram_id = Column(Integer, ForeignKey('games.telegram_id'), primary_key=True, nullable=False)
    color_victory = Column(String(5),nullable=False)
    block_num = Column(SMALLINT, nullable=False)
    block_height = Column(String(60), nullable=False)
    balance = Column(Numeric(19, 7), nullable=False)
    vinner_telegram_id = Column(Integer, nullable=False)

    game_id_2relat = relationship("Game", back_populates="rounds_game_ids")
    game_creator_telegram_id = relationship("Game", back_populates="rounds_creator_telegram_ids")

    def __init__(self, round_id, games_id, creator_telegram_id, color_victory, block_num, block_heigth,
                 balance, vinner_telegram_id):
        self.round_id = round_id
        self.games_id = games_id
        self.creator_telegram_id = creator_telegram_id
        self.color_victory = color_victory
        self.block_num = block_num
        self.block_height = block_heigth
        self.balance = balance
        self.vinner_telegram_id = vinner_telegram_id
