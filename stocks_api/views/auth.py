from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class AuthAPIView(APIViewSet):
    '''This class displays the api endpoint message. It is not built out yet, as it needs
    actual functionality besides just sending jsons.
    '''

    def create(self, request, id=None):
        return Response(json={'message': f'Created a single auth resource for {id}'})
