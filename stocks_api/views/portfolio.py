from ..models.schemas import PortfolioSchema
from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError, DataError
from pyramid.view import view_config
from pyramid.response import Response
from ..models import Portfolio, Account
import requests
import json

class PortfolioAPIView(APIViewSet):
    '''This class displays the api endpoint message. It is not built out yet, as it needs
    actual functionality besides just sending jsons.
    '''
    def create(self, request):
        """This method checks to see if the user correctly implimented the syntax for creating
        a new portfolio. If the syntax is correct, it then checks to see if the portfolio already
        exists in the database. If the portfolio name is new, then the portfolio is created and tied
        to the current user.
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'name' not in kwargs:
            return Response(json='Expected value: name', status=400)
        import pdb; pdb.set_trace()
        if request.authenticated_userid:
            account = Account.one(request, request.authenticated_userid)
            kwargs['account_id'] = account.id


        try:
            portfolio = Portfolio.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error. Portfolio already exists', status=409)

        schema = PortfolioSchema()
        data = schema.dump(portfolio).data

        return Response(json=data, status=201)
