import os
import sys
import logging

import tornado.websocket
import tornado.web
import tornado.wsgi


logger = logging.getLogger("ws")


sys.path = ["."] + sys.path
os.environ["DJANGO_SETTINGS_MODULE"] = "Compare.settings"

    
class CompareYoutubeWSHandler(tornado.websocket.WebSocketHandler):
    
    def open(self):
        logger.debug("socket opened")
      
    def on_message(self, message):
        logger.debug("message %s received")
        self.write_message(u"You said: " + message)
        
    def on_close(self):
        logger.debug("socket closed")
        
        
urls = [
    (r"/youtube", CompareYoutubeWSHandler),
]


# For testing
if __name__ == "__main__":
    import tornado.ioloop
    
    application = tornado.web.Application(urls)

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
else:
    application = tornado.wsgi.WSGIApplication(urls)
    