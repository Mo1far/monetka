from sqlalchemy import Column, Integer, String, Table
from sqlalchemy import ForeignKey

from .base import Base

association_table = Table('tokens_riskpool', Base.metadata,
    Column('totens_token', String(50), ForeignKey('tokens.token')),
    Column('tokens_wallet_id', Integer, ForeignKey('tokens.wallet_id')),
    Column('riskpool_rp_id', Integer, ForeignKey('riskpool.rp_id'))
)