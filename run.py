#!/usr/bin/env python

import wsgiref.simple_server
from tornado.options import define, options
from app import Application


define("port", default=5000, help="run on the given port", type=int)


if __name__ == "__main__":
    print 'Listening on port %d' % options.port
    server = wsgiref.simple_server.make_server('', options.port, Application())
    server.serve_forever()
