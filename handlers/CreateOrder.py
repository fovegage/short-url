# -*- coding: utf-8 -*-
from .BaseHandler import BaseHandler
import urllib
import hashlib
from uuid import uuid1
from utils.GenCode import PayCode


class Order(BaseHandler):
    def post(self, *args, **kwargs):
        out_trade_no = self.get_argument('out_trade_no')
        total_fee = self.get_argument('total_fee')
        subject = self.get_argument('subject')
        body = self.get_argument('body')

        pay_data = {
            'out_trade_no': out_trade_no,
            'total_fee': total_fee,
            'subject': subject,
            'body': body,
        }

        out_order_id = self.db.payinfo.find_one({'out_order_id': pay_data['out_trade_no']})

        if out_order_id == None:
            call = str(uuid1())
            self.write(call)
            p = PayCode(pay_data['subject'], pay_data['total_fee']).GetCode()
            info = {'pay_id': call, 'qr_id': p[1],
                    'qr_code': p[0], 'out_order_id': pay_data['out_trade_no'],
                    'subject': pay_data['subject'], 'body': pay_data['body'],
                    'fee': pay_data['total_fee']
                    }
            self.db.payinfo.insert_one(info)
        else:
            self.write(str(self.db.payinfo.find_one({'out_order_id': pay_data['out_trade_no']})['pay_id']))

