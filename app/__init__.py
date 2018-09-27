#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  tornado application
"""
from tornado.web import Application
from tornado_sqlalchemy import make_session_factory

from config import CONFIG
from url_mapping import ROUTES


class App(Application):
  def __init__(self,config):
    tornado_settings = config.TORNADO_SETTINGS
    print(tornado_settings)
    print(ROUTES)
    session_factory = make_session_factory(config.MYSQL_URI)
    Application.__init__(self, handlers=ROUTES, session_factory=session_factory,**tornado_settings)


def create_app():
  app = App(CONFIG)
  return app
