from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class PortfolioAPIView(APIViewSet):

    def retrieve(self, request, id):
        return Response(json={'message': f'Retrieving portfolio from {id}'}, status=200)
