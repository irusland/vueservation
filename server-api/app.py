import os
import urllib

import magic
from ihttpy.exceptions.logger import LogLevel
from ihttpy.httpserver import Server
from ihttpy.requests.methods import Method
from ihttpy.requests.request import Request
from ihttpy.requests.response import Response
from ihttpy.routing.configurator import FluentConfigurator
from ihttpy.requests.sender import handle as send_file

from handlers.restaurants_api import get_restaurants, get_restaurant
from handlers.users_api import get, preflight
from handlers.orders_api import order, get_all, get_info, validate, preflight

config = FluentConfigurator()


@config.on(Method.GET).at('/')
def index(req: Request, srv: Server):
    body = urllib.parse.unquote(req.path).encode()
    headers = [
        ('Content-Type', f'text/txt'),
        ('Content-Length', len(body))
    ]
    return Response(200, 'OK', headers, body)


@config.on(Method.GET).at('/restaurants')
def get_restaurants_bp(*a, **k):
    return get_restaurants(*a, **k)


@config.on(Method.GET).at('/restaurants/data')
def get_restaurant_bp(*a, **k):
    return get_restaurant(*a, **k)


@config.on(Method.GET).at('/pictures/[name].[ext]')
def send_bp(req: Request, srv: Server):
    name = req.path.split('/')[-1]
    mime = magic.Magic(mime=True)
    filepath = os.path.join('pictures', name)
    content_type = mime.from_file(filepath)
    return Response.build_file_res(req, filepath, content_type)


@config.on(Method.GET).at('/users')
def user_bp(*a, **k):
    return get(*a, **k)


@config.on(Method.POST).at('/orders')
def orders_bp(*a, **k):
    return order(*a, **k)


@config.on(Method.OPTIONS).at('/orders')
def pre_orders_bp(*a, **k):
    return preflight(*a, **k)









if __name__ == '__main__':
    config._host = '0.0.0.0'
    config._port = 8000
    server = Server(config, loglevel=LogLevel.CONSOLE)
    with server as s:
        s.run()
