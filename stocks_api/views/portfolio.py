from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class PortfolioAPIView(APIViewSet):
    '''This class displays the api endpoint message. It is not built out yet, as it needs
    actual functionality besides just sending jsons.
    '''

    def retrieve(self, request, id):
        return Response(json={'message': 'Retrieving single portfolio from Portfolio API'}, status=200)
