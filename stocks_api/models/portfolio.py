from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import relationship
from sqlalchemy import(
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    Float,
    ForeignKey
)

from .meta import Base


class Portfolio(Base):
    """This creates a new portfolio when invoked.
    The portfolio table has columns of portfolio ID, portfolio Name, date created,
    date updated, and the corresponding account tied to the portfolio.
    """
    __tablename__ = 'portfolio'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    accounts = relationship('Account', back_populates='portfolio')

    @classmethod
    def new(cls, request, **kwargs):
        """This creates a new instance of a portfolio.
        """
        if request.dbsession is None:
            raise DBAPIError
        # weather = WeatherLocation({'name': 'some name', 'zip_code': 98012})
        # weather = cls(**kwargs)
        # request.dbsession.add(weather)
        portfolio = cls(**kwargs)
        request.dbsession.add(portfolio)

        return request.dbsession.query(cls).filter(
            cls.name == kwargs['name']).one_or_none()

    @classmethod
    def one(cls, request, pk=None):
        """This creates a GET request to the portfolio database and returns the requested
        portfolio.
        """
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk)

