# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 9:20
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : auth.py
# @Software: PyCharm

# 鉴权
class Auth():
    def __init__(self):
        pass


class Sign(Auth):
    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret

    def get_app_id(self):
        return self.app_id

    def get_app_secret(self):
        return self.app_secret


class Token(Auth):
    def __init__(self, token):
        self.token = token

    def get_token(self):
        return self.token