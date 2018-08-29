from .meta import Base
from sqlalchemy.orm import relationship
from .associations import roles_association
from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
)

class AccountRole(Base):
    """
    """
    __tablename__ = 'account_roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    accounts = relationship('Account', secondary=roles_association, back_populates='roles')