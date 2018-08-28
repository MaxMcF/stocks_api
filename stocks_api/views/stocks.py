from ..models.schemas import StocksInfoSchema
from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError, DataError
from pyramid.view import view_config
from pyramid.response import Response
from ..models import StocksInfo
import requests
import json

API_URL = 'https://api.iextrading.com/1.0/'

@view_config(route_name='lookup', renderer='json', request_method='GET')
def lookup(request):
    """This is going to listen to a request from a specific endpoint.
    """
    symbol = request.matchdict['symbol']
    url = f'{API_URL}stock/{symbol}/chart'
    response = requests.get(url)

    return Response(json=response.json(), status=200)


class StocksAPIView(APIViewSet):
    '''This class displays the api endpoint message. It is not built out yet, as it needs
    actual functionality besides just sending jsons.
    '''

    def create(self, request):
        """
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'symbol' not in kwargs:
            return Response(json='Expected value: symbol', status=400)
        try:
            stock = StocksInfo.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error. Stock already exists', status=409)

        schema = StocksInfoSchema()
        data = schema.dump(stock).data

        return Response(json=data, status=201)

    def retrieve(self, request, id=None):
        return Response(json={'message': 'Retrieving single stock record from stocks API'}, status=200)

    def destroy(self, request, id=None):
        """
        """
        if not id:
            return Response(json='Not Found', status=404)

        try:
            StocksInfo.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        return Response(status=204)
