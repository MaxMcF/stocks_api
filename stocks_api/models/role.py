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
    """This creates a many to many ID relationship within the account roles table.
    Since multiple accounts can have the same role, and since each account can have multiple
    roles, a many-to-many table is necessary.
    """
    __tablename__ = 'account_roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    accounts = relationship('Account', secondary=roles_association, back_populates='roles')
