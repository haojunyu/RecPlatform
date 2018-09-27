#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import *

class User(Base):
  __tablename__ = 'users'

  id = Column('id', Integer, primary_key=True)
  name = Column('name', String(64), nullable=False)
  passwd = Column('passwd', String(64), nullable=False)
  email = Column(String(32), nullable=False, unique=True)

  def __repr__(self):
    return "User %r" % self.name

  def to_json(self):
    json_user = {
      'id'   : self.id,
      'name' : self.name,
      'email': self.email
    }
    return json_user

  @staticmethod
  def from_json(json_user):
    name = json_user.get('name')
    passwd = json_user.get('passwd')
    email = json_user.get('email')
    return User(name=name,passwd=passwd,email=email)

  @staticmethod
  def gen_users():
    user = User(id=1,name='hjy',passwd='hjy',email='haojunyu2012@gmail.com')

