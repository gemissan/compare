import os
import sys

import tornado.websocket
import tornado.web
import tornado.wsgi


sys.path = ["."] + sys.path
os.environ["DJANGO_SETTINGS_MODULE"] = "Compare.settings"

    
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.write_message("Hello")
      
    def on_message(self, message):
        pass
 
    def on_close(self):
        pass
  
  

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello")
  

application = tornado.wsgi.WSGIApplication(
    [
     (r"/ws/hello", HelloHandler),
     (r"/ws", WebSocketHandler),
     ])

