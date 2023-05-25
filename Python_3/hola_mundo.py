from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def hola_mundo(request):
    return Response('Hola Mundo!' % request.matchdict)

config = Configurator()

config.add_route('hola', '/hola')
config.add_view(hola_mundo, route_name='hola')


app = config.make_wsgi_app()
server = make_server('0.0.0.0', 8081, app)
server.serve_forever()
