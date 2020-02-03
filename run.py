from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from flaskr import create_app

http_server = HTTPServer(WSGIContainer(create_app))
http_server.listen(8888)
http_server.start(0)
IOLoop.instance().start()