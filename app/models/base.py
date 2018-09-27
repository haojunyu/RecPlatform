#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Date, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
from tornado_sqlalchemy import declarative_base

Base = declarative_base()
