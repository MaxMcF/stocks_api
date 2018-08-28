from marshmallow_sqlalchemy import ModelSchema
from . import StocksInfo
# from . import Portfolio
from .portfolio import Portfolio


class StocksInfoSchema(ModelSchema):
    class Meta:
        model = StocksInfo

class PortfolioSchema(ModelSchema):
    class Meta:
        model = Portfolio
