import ihttpy
from ihttpy.exceptions.logger import LogLevel
from ihttpy.httpserver import Server
from ihttpy.routing.configurator import FluentConfigurator
from ihttpy.requests.request import Request
from ihttpy.requests.methods import Method


configure = FluentConfigurator()


@configure.on(Method.GET).at('/')
def index(req: Request, server: Server):
    print(req.path, req.method)


if __name__ == '__main__':
    configure._host = '0.0.0.0'
    configure._port = 8080
    server = Server(
        configurator=configure,
        loglevel=LogLevel.CONSOLE,
    )
    with server as s:
        s.run()
