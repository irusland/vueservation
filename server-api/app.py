import urllib

from ihttpy.exceptions.logger import LogLevel
from ihttpy.httpserver import Server
from ihttpy.requests.request import Request
from ihttpy.requests.response import Response
from ihttpy.requests.methods import Method
from ihttpy.routing.configurator import FluentConfigurator


configure = FluentConfigurator()


@configure.on(Method.GET).at('/getonly')
@configure.on(Method.GET | Method.OPTIONS).at('/index')
@configure.on(Method.POST).at('/post')
def index(request: Request, srv: Server = None):
    body = f'{request.method} ready for {request.path}'
    headers = [
        ('Content-Type', f'text/txt'),
        ('Content-Length', len(body))
    ]
    response = Response(200, 'OK', headers=headers, body=body.encode())
    print('<\n', response)
    return response


@configure.on(Method.GET).at('/[f].[e]')
def f(req: Request, srv: Server):
    body = urllib.parse.unquote(req.path)
    headers = [
        ('Content-Type', f'text/txt'),
        ('Content-Length', len(body))
    ]
    response = Response(200, 'OK', headers=headers, body=body.encode())
    print('<\n', response)
    return response


if __name__ == '__main__':
    configure._host = '0.0.0.0'
    configure._port = 8080
    server = Server(
        configurator=configure,
        loglevel=LogLevel.CONSOLE,
    )
    with server as s:
        s.run()