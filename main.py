# -*- coding: utf-8 -*-

import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
from tornado.options import define, options
import pymongo
from settings import path, mongo
from urls import urls
define('port', type=int, default=11111, help='Please run on this port.')

class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.db = pymongo.MongoClient(**mongo)

def main():
    tornado.options.parse_command_line()
    app = Application(
        handlers=urls,
        **path
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()



if __name__ == '__main__':
    main()