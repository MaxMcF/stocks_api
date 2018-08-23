from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class CompanyAPIView(APIViewSet):
    '''This class displays the api endpoint message. It is not built out yet, as it needs
    actual functionality besides just sending jsons.
    '''

    def retrieve(self, request, id=None):
        return Response(json={'message': f'Provided a single resource for {id}'}, status=200)
