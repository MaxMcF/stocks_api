from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class StocksAPIView(APIViewSet):

    def create(self, request):
        return Response(json={'message': 'Creating a single stock record'}, status=201)

    def retrieve(self, request, id):
        return Response(json={'message': f'Retrieving stock record from {id}'}, status=200)

    def destroy(self, request, id):
        return Response(status=204)
