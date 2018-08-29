from .portfolio import Portfolio
from sqlalchemy.orm import relationship
from .role import AccountRole
from .associations import roles_association
from .meta import Base
from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import(
    Column,
    Index,
    Integer,
    String,
    Text,
    DateTime,
)

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    email = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    portfolio = relationship(Portfolio, back_populates='accounts')
    roles = relationship(AccountRole, secondary=roles_association, back_populates='accounts')
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    def __init__(self, email, password=None):
        self.email = email
        self.password = password #Not safe, must fix

    @classmethod
    def new(cls, request, email=None, password=None):
        """Register a new user.
        """
        if not request.dbsession:
            raise DBAPIError
        user = cls(email, password)
        request.dbsession.add(user)

        #TODO Assign Roles to new user

        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def check_credentials(cls, request, email, password):
        """Validate that the user is who they say they are, checking if they exist.
        """
        # TODO: complete this tomorrow as part of login process
        pass




