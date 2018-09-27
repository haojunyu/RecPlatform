#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler
from tornado_sqlalchemy import SessionMixin, as_future

class BaseHandler(SessionMixin, RequestHandler):
  pass
