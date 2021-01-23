import sqlalchemy as sa
from sqlalchemy.orm import relationship

from db import Base

class Item(Base):
    __tablename__ = 'items'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    name = sa.Column(sa.String(100))
    description = sa.Column(sa.String, index=True, nullable=True)
    price = sa.Column(sa.Integer, index=True)

    owner_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), index=True)
    owner = relationship('User', back_populates='item')