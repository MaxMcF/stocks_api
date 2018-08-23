from pyramid_restful.routers import ViewSetRouter
from .views.stocks import StocksAPIView

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('portfolio', '/portfolio')

    router = ViewSetRouter(config)
    router.register('api/v1/stocks', StocksAPIView, 'stocks')
