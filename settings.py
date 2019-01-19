# -*- coding: utf-8 -*-
import os

# 有赞云支付配置
youzan = {
    'client_id': '有赞云id',
    'client_secret': '有赞云密钥',
    'grant_type': 'silent',  # 请勿修改
    'kdt_id': '店铺id'
}

# MongoDB配置
mongo = {
    'host': 'localhost',
    'port': 27017
}

# 项目路径
path = {
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'cookie_secret': 'lonqS8z4RB6CENU+jEPvLqjXbinxQEsJlTwdp/ehx9Y=',
    # 'xsrf_cookies': True,
    'debug': True
}
