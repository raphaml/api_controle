import sqlalchemy as sa
from sqlalchemy.orm import relationship

from db import Base

class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    email = sa.Column(sa.String, unique=True, index=True)
    hashed_password = sa.Column(sa.String)
    name = sa.Column(sa.String(100))
    created_at = sa.Column(sa.DateTime(timezone=True), default=sa.func.now())
    is_active = sa.Column(sa.Boolean, default=True)

    item = relationship('Item', back_populates='owner')