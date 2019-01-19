# -*- coding: utf-8 -*-
import requests
import json
from settings import youzan

class GetToken():
    def __init__(self):
        self.url = 'https://open.youzan.com/oauth/token'
        self.data = youzan
        self.headers = {
            'content - type': 'application/x-www-form-urlencoded'
        }

    def token(self):
        tokeninfo = requests.post(self.url, headers=self.headers, data=self.data)
        return json.loads(tokeninfo.text)['access_token']
