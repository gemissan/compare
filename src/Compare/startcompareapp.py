import os
import sys

from tornado.options import options, define
import django.core.handlers.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.websocket
import tornado.wsgi


sys.path = ["."] + sys.path
os.environ["DJANGO_SETTINGS_MODULE"] = "Compare.settings"


define('port', type=int, default=8000)

    
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.write_message("Hello World")
      
    def on_message(self, message):
        pass
 
    def on_close(self):
      pass


def main():
  django_app = tornado.wsgi.WSGIContainer(django.core.handlers.wsgi.WSGIHandler())
  app = tornado.web.Application(
    [
      ('/ws', WebSocketHandler),
      ('.*', tornado.web.FallbackHandler, dict(fallback=django_app)),
      ])
  server = tornado.httpserver.HTTPServer(app)
  server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
  main()
