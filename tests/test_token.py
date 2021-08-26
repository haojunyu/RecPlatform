#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from app import *

class TokenTestCase(unittest.TestCase):
  # 初始化工作
  def setUp(self):
    pass

  # 退出清理工作
  def tearDown(self):
    pass

  # 测试token生成
  def test_gen_token(self):
    user = User(id=1,name='hjy',passwd='hjy',email='haojunyu2012@gmail.com')
    token = user.generate_auth_token()
    print(token)
    info = User.verify_auth_token(token)
    print(info)
    self.assertEqual(info['name'],'hjy')
