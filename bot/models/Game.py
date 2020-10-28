from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from bot.models.Round_info import Round_info
Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    telegram_id = Column(Integer, ForeignKey('users.telegram_id'), primary_key=True, nullable=False)
    token_type = Column(String(10), nullable=False)

    user = relationship('User', back_populates='games')

    rounds_game_ids = relationship("Rounds_info", order_by=Round_info.game_id, back_populates="game_id_2relat")
    rounds_creator_telegram_ids = relationship("Rounds_info", order_by=Round_info.creator_telegram_id,
                                               back_populates="game_creator_telegram_id")

    def __init__(self, telegram_id, token_type):
        self.telegram_id = telegram_id
        self.token_type = token_type

