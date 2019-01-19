# -*- coding: utf-8 -*-

from handlers import CreateOrder, PayOrder, QueryOrder, SaveOrder
urls = [
    (r'/add', CreateOrder.Order),
    (r'/pay(\S+)', PayOrder.Pay),
    (r'/query', QueryOrder.websocket),
    (r'/ls', SaveOrder.Query),
    (r'/notice', SaveOrder.Notice)
]
