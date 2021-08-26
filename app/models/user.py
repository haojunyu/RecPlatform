#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import *
from config import CONFIG
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class User(Base):
  __tablename__ = 'users'

  id = Column('id', Integer, primary_key=True)
  name = Column('name', String(64), unique=True, nullable=False)
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
    init_users = []
    user = User(id=1,name='hjy',passwd='hjy',email='haojunyu2012@gmail.com')
    init_users.append(user)
    return init_users


  # 生成授权token
  def generate_auth_token(self, expiration=3600):
    s = Serializer(CONFIG.SECRET_KEY, expires_in=expiration)
    return s.dumps({'name':self.name})

  # 验证授权token
  @staticmethod
  def verify_auth_token(token):
    s = Serializer(CONFIG.SECRET_KEY)
    try:
      data = s.loads(token)
      print(data)
    except:
      data = None
    return data
