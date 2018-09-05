from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import(
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    Float
)

from .meta import Base

class StocksInfo(Base):
    """This creates a new instance of a company stock, which uses the information
    taken from the IEX API. The information received from the IEX API gets
    company info of stock symbol, company name, exchange venue, industry, website,
    description, CEO name, stock issue type, and sector. This class also logs the
    date this stock was put into the local database, as well as the date updated.
    """
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    symbol = Column(Text)
    company_name = Column(Text)
    exchange = Column(Text)
    industry = Column(Text)
    website = Column(Text)
    description = Column(Text)
    CEO = Column(Text)
    issue_type = Column(Text)
    sector = Column(Text)
    # zip_code = Column(Integer, unique=True, nullable=False)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    @classmethod
    def new(cls, request, **kwargs):
        """This creates a new stock in the stocks table within your local database.
        """
        if request.dbsession is None:
            raise DBAPIError
        # weather = WeatherLocation({'name': 'some name', 'zip_code': 98012})
        # weather = cls(**kwargs)
        # request.dbsession.add(weather)
        stock = cls(**kwargs)
        request.dbsession.add(stock)
        return request.dbsession.query(cls).filter(
            cls.symbol == kwargs['symbol']).one_or_none()

    @classmethod
    def all(cls, request):
        """This GET request gets all of the stocks that have been stored in the local database.
        """
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).all()

    @classmethod
    def one(cls, request, pk=None):
        """This GET request gets one stock based on the corresponding ID within the local database.
        """
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk)

    @classmethod
    def remove(cls, request, pk=None):
        """This performs a DELETE request to the local database, using the ID of the stock in question.
        """
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).filter(
            cls.accounts.email == request.authenticated_userid
            ).filter(cls.id == pk).delete()

