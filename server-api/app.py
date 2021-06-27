import os
import urllib

import magic
from ihttpy.exceptions.logger import LogLevel
from ihttpy.httpserver import Server
from ihttpy.requests.methods import Method
from ihttpy.requests.request import Request
from ihttpy.requests.response import Response
from ihttpy.routing.configurator import DecorativeConfigurator

from handlers.restaurants_api import get_restaurants, get_restaurant
from handlers.users_api import get, preflight
from handlers.orders_api import order, get_all, get_info, validate, preflight


config = DecorativeConfigurator()


@config.rule(Method.GET, '/')
def index(req: Request, srv: Server):
    body = urllib.parse.unquote(req.path).encode()
    headers = [
        ('Content-Type', f'text/txt'),
        ('Content-Length', len(body))
    ]
    return Response(200, 'OK', headers, body)


@config.rule(Method.GET, '/restaurants')
def get_restaurants_bp(*a, **k):
    return get_restaurants(*a, **k)


@config.rule(Method.GET, '/restaurants/data')
def get_restaurant_bp(*a, **k):
    return get_restaurant(*a, **k)


@config.rule(Method.GET, '/pictures/[name].[ext]')
def send_bp(req: Request, srv: Server):
    name = req.path.split('/')[-1]
    mime = magic.Magic(mime=True)
    filepath = os.path.join('pictures', name)
    content_type = mime.from_file(filepath)
    return Response.build_file_res(req, filepath, content_type)


@config.rule(Method.GET, '/users')
def user_bp(*a, **k):
    return get(*a, **k)


@config.rule(Method.POST, '/orders')
def orders_bp(*a, **k):
    return order(*a, **k)


@config.rule(Method.OPTIONS, '/orders')
def pre_orders_bp(*a, **k):
    return preflight(*a, **k)


@config.rule(Method.GET, '/orders/accept-[hash]')
def order_validate_bp(*a, **k):
    return validate(*a, **k)


@config.rule(Method.GET, '/orders/[id]')
def order_bp(*a, **k):
    return get_info(*a, **k)


@config.rule(Method.GET, '/orders')
def orders_all_bp(*a, **k):
    return get_all(*a, **k)


if __name__ == '__main__':
    config._host = '0.0.0.0'
    config._port = 8000
    server = Server(config, loglevel=LogLevel.CONSOLE)
    with server as s:
        s.run()
