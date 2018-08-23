from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class PortfolioAPIView(APIViewSet):

    def list(self, request):
        return Response(json={'message': 'Listing all the portfolios'}, status=200)

    def create(self, request):
        return Response(json={'message': 'Creating a single portfolio item'}, status=201)

    def destroy(self, request, id):
        return Response(status=204)
