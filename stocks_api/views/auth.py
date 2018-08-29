from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError
from pyramid.response import Response
from ..models import Account
import json


class AuthAPIView(APIViewSet):
    '''This class displays the api endpoint message. It is not built out yet, as it needs
    actual functionality besides just sending jsons.
    '''
    # import pdb; pdb.set_trace()

    def create(self, request, auth=None):
        """
        """
        import pdb; pdb.set_trace()
        data = json.loads(request.body)
        if auth == 'register':
            try:
                user = Account.new(
                    request,
                    data['email'],
                    data['password'],
                )
            except (IntegrityError, KeyError):
                return Response(json='Bad Request', status=400)
            # TODO refactor to use a json web token
            return Response(json='Created', status=201)

        if auth == 'login':

            pass

        return Response(json='AUTH Not Found', status=404)
