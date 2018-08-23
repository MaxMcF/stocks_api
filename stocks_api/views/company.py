from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class CompanyAPIView(APIViewSet):

    def retrieve(self, request, id=None):
        return Response(json={'message': f'Provided a single resource for {id}'}, status=200)
