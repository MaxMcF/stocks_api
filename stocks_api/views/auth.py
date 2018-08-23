from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class AuthAPIView(APIViewSet):

    def create(self, request, id=None):
        return Response(json={'message': f'Created a single resource for {id}'})
