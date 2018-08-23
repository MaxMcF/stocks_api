from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class StocksAPIView(APIViewSet):

    def list(self, request):
        return Response(json={'message': 'Listing all the records'}, status=200)

    def create(self, request):
        return Response(json={'message': 'Creating a single record'}, status=201)

    def retrieve(self, request, id):
        return Response(json={'message': f'Retrieving record from {id}'}, status=200)


