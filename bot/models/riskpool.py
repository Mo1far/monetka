from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .token_riskpool import Association_table
class Riskpool(Base):
    __tablename__ = 'riskpool'

    rp_id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)

    def __init__(self, rp_id):
        self.rp_id = rp_id

