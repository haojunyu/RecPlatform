#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  tornado application
"""
from tornado.web import Application
from tornado_sqlalchemy import make_session_factory

from config import CONFIG
from url_mapping import ROUTES
from app.models import *

session_factory = make_session_factory(CONFIG.MYSQL_URI)

def init_data():
  session = session_factory.make_session()
  init_users = User.gen_users()
  for user in User.gen_users():
    session.add(user)
  try:
    session.commit()
    print('generate users successfully')
  except IntegrityError:
    session.rollback()
    print('faill to generate users')


class App(Application):
  def __init__(self,config):
    tornado_settings = config.TORNADO_SETTINGS
    print(tornado_settings)
    print(ROUTES)
    Application.__init__(self, handlers=ROUTES, session_factory=session_factory,**tornado_settings)


def create_app():
  app = App(CONFIG)
  return app
