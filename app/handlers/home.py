#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.gen import coroutine

from .base import *
from app.models import *

class HomeHandler(BaseHandler):
  @coroutine
  def get(self):
    with self.make_session() as session:
      count = yield as_future(session.query(User).count)
      print(count)

    self.write('asbdsdsf')
