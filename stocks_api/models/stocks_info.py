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
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).all()

    @classmethod
    def one(cls, request, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk)

    @classmethod
    def remove(cls, request, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk).delete()
