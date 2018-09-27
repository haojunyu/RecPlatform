#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    application runner
"""
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options,define,parse_command_line
from app import create_app


define('host', default='0.0.0.0', type=str, help='server bind host')
define('port', default=51888, type=int, help='server bind port')


def run(host, port):
  app = create_app()
  http_server = HTTPServer(app)
  http_server.listen(port, address=host)
  IOLoop.instance().start()


if __name__ == '__main__':
  parse_command_line()
  run(options.host, options.port)


