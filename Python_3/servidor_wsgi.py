from wsgiref.simple_server import make_server

def simple_app(environ, start_response):
    status = '200 OK'
    header = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, header)
    ret = b"<html><body><h2>Hola Mundo</h2></body></html>"
    return [(ret)]

if __name__ == '__main__':
    httpd = make_server('', 8080, simple_app)
    print("Lanzando servidor en puerto 8080...")
    httpd.serve_forever()
