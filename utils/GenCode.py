# -*- coding: utf-8 -*-
from libs.youzan import auth, client
from utils.Token import GetToken
import json


class PayCode():

    def __init__(self, name, price):

        self.token = auth.Token(token=GetToken().token())
        self.client = client.YZClient(self.token)
        self.params = {}
        self.files = []
        self.name = name
        self.price = price

    def GenCode(self):
        self.params['qr_name'] = self.name
        self.params['qr_price'] = float(self.price) * 100
        self.params['qr_type'] = "QR_TYPE_DYNAMIC"
        return self.client.invoke('youzan.pay.qrcode.create', '3.0.0', 'GET', params=self.params,
                                  files=self.files).decode('utf-8')

    def GetCode(self):
        codeinfo = json.loads(self.GenCode())['response']
        return codeinfo['qr_code'], codeinfo['qr_id']

