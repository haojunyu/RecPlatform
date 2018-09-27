#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import url, StaticFileHandler
from app.handlers import *


ROUTES = [
  # index
  url(r"/", HomeHandler, name='index'),
  url(r'/favicon.ico', StaticFileHandler, {'path': 'static/favicon.ico'}),
]
