# -*- coding: utf-8 -*-
import tornado.websocket
import pymongo
import time

def mongo():
    client = pymongo.MongoClient("localhost", 27017)
    return client.pay

class ProStatus(object):
    ''' 处理类 '''

    w_register = []

    def register(self, callbacker):
        ''' 记录客户端连接实例 '''
        self.w_register.append(callbacker)

    def unregister(self, callbacker):
        ''' 删除客户端连接实例 '''
        self.w_register.remove(callbacker)

    def makelines(self, lines):
        ''' 处理接受的行内容 '''
        pass

    def trigger(self, line):
        pass


class websocket(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self, *args, **kwargs):
        ProStatus().register(self)

    def close(self, code=None, reason=None):
        ProStatus().unregister(self)  # 删除客户端连接

    def on_message(self, message):
        codeinfo = mongo().payinfo.find_one({'qr_id': str(message)}, {"_id": 0})
        self.write_message(codeinfo)
