#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  tornado application
"""
from tornado.web import Application

from config import CONFIG
from url_mapping import ROUTES


class App(Application):
  def __init__(self,config):
    tornado_settings = config.TORNADO_SETTINGS
    print(tornado_settings)
    print(ROUTES)
    Application.__init__(self, handlers=ROUTES, **tornado_settings)


def create_app(config_name):
  config = CONFIG[config_name]
  app = App(config)
  return app
