from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class StocksAPIView(APIViewSet):
    '''This class displays the api endpoint message. It is not built out yet, as it needs
    actual functionality besides just sending jsons.
    '''

    def create(self, request):
        return Response(json={'message': 'Creating a single stock record'}, status=201)

    def retrieve(self, request, id):
        return Response(json={'message': 'Retrieving single stock record from stocks API'}, status=200)

    def destroy(self, request, id):
        return Response(status=204)
