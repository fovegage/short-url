# -*- coding: utf-8 -*-
from .BaseHandler import BaseHandler
from .SaveOrder import Judge


class Pay(BaseHandler):

    def get(self, s):
        pay_id = str(s).lstrip('/')
        payinfo = self.db.payinfo.find_one({'pay_id': pay_id})
        if payinfo:
            subject = payinfo['subject']
            out_order_id = payinfo['out_order_id']
            fee = payinfo['fee']
            body = payinfo['body']
            qr_code = payinfo['qr_code']
            qr_id = payinfo['qr_id']
            tid = Judge(qr_id).GetTid()
            self.db.payinfo.update_one({'qr_id': qr_id}, {'$set': {'tid': tid}})
            self.render('pay.html', subject=subject, orderid=out_order_id, fee=fee, id=qr_id, body=body,
                        code=qr_code, codeid=pay_id)
        else:
            self.write({'error': -1, 'status': "pay_id i'not exist"})
