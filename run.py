from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import flaskr

http_server = HTTPServer(WSGIContainer(flaskr.create_app()))
http_server.listen(8888)
http_server.start(0)
IOLoop.instance().start()