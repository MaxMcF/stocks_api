from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='home', renderer='json', request_method='GET')
def home_view(request):
    """Displays the landing page of this webpage. This shows the possible API calls

        Args:
            requst- This is the GET request that is linked to the '/' path, which is the
                    landing page.
        Return:
            A message containing the possible api route calls
            A status message of 200, which is not necessary to specify since its implied
                >Im doing this anyway to remember Response takes in this argument.
    """
    message = '''
    GET / - the base API route
    POST /api/v1/auth/ - for registering a new account and signing up
    GET /api/v1/portfolio/{id}/ - for retrieving a user's portfolio
    POST /api/v1/stock/ - for creating a new company record
    GET /api/v1/stock/{id}/ - for retrieving a companies information
    DELETE /api/v1/stock/{id} - for deleting a company record
    GET /api/v1/company/{symbol} - for retrieving company detail from 3rd party API, where `{symbol}` is variable
    '''
    return Response(body=message, content_type='text/plain', status=200)
