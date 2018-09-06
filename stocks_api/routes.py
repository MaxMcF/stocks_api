from pyramid_restful.routers import ViewSetRouter
from .views import StocksAPIView, PortfolioAPIView, CompanyAPIView, AuthAPIView, VisualAPIView

def includeme(config):
    '''This is the main routes page. This utilizes pyramid restful routes to link the requests
    to the corresponding API class views.
    '''
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('lookup', '/api/v1/lookup/{symbol}')

    router = ViewSetRouter(config, trailing_slash=False)
    router.register('api/v1/stock', StocksAPIView, 'stock')
    router.register('api/v1/company', CompanyAPIView, 'company', permission='admin')
    router.register('api/v1/portfolio', PortfolioAPIView, 'portfolio')
    router.register('api/v1/auth/{auth}', AuthAPIView, 'auth')
    router.register('api/v1/visuals', VisualAPIView, 'view')
