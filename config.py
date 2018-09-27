#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or '5bf030dbb13422031ea802a9ab75900a'
  TORNADO_SETTINGS = {
    'debug'       : None,
    'static_path' : os.path.join(PROJECT_ROOT,'static'),
    'xsrf_cookies': True
  }
  MYSQL_URI = None


# 开发环境配置
class DevelopmentConfig(Config):
  Config.TORNADO_SETTINGS['debug'] = False
  MYSQL_URI = 'mysql://recsys:recsys@localhost/RecSys'

# 线上环境配置
class ProductionConfig(Config):
  Config.TORNADO_SETTINGS['debug'] = True
  MYSQL_URI = 'mysql://recsys:recsys@localhost/RecSys'


CONFIG = {
  'development' : DevelopmentConfig,
  'production'  : ProductionConfig,
  'default'     : DevelopmentConfig
}
