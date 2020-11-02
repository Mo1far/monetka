from sqlalchemy import Column, Integer, String, Table
from sqlalchemy import ForeignKey

from .base import Base

class Association_table(Base):
    __tablename__ = 'tokens_riskpool'

    totens_token = Column(String(50), ForeignKey('tokens.token'), primary_key=True)
    tokens_wallet_id = Column(Integer, ForeignKey('tokens.wallet_id'), primary_key=True)
    riskpool_rp_id = Column(Integer, ForeignKey('riskpool.rp_id'), primary_key=True)
