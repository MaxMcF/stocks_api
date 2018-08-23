from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class AuthAPIView(APIViewSet):

    def retrieve(self, request, symbol=None):
        return Response(json={'message': f'Provided a single resource for {symbol}'})
