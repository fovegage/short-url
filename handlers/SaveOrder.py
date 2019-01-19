# -*- coding: utf-8 -*-
from .BaseHandler import BaseHandler
from libs.youzan import auth, client
from utils.Token import GetToken
import json
from urllib import parse

class Notice(BaseHandler):
    """接收有赞云推送"""

    def post(self, *args, **kwargs):
        notice = json.loads(self.request.body)
        # 收到推送立即向有赞云服务器推送成功消息
        if notice:
            self.write({"code": 0, "msg": "success"})
        if notice['status'] == 'TRADE_PAID':
           url_data = parse.unquote(notice['msg'])  
           qr_info = json.loads(url_data)['qr_info']
           qr_id = qr_info['qr_id']
           print(qr_id)
           self.db.payinfo.update_one({'qr_id': str(qr_id)}, {'$set': {'flag': 'TRADE_PAID'}})


class Judge():

    def __init__(self, qr_id):
        self.token = auth.Token(token=GetToken().token())
        self.client = client.YZClient(self.token)
        self.qr_id = qr_id
        self.invoke = json.loads(self.client.invoke('youzan.trades.qr.get', '3.0.0', 'GET'))
        # self.invoke1 = json.loads(self.client.invoke('youzan.pay.qrcodes.get', '3.0.0', 'GET'))

    def TradeList(self):
        """获取交易条数"""
        return self.invoke['response']['total_results']

    def JudgePay(self):
        """获取指定的交易信息"""
        return ([i for i in self.invoke['response']['qr_trades'] if i['qr_id'] == self.qr_id])

    def ListPay(self):
        """获取全部交易列表"""
        return self.invoke['response']['qr_trades']

    def QR_ID(self):
        return ([i['qr_id'] for i in self.invoke['response']['qr_trades']])

    def Query_Status(self):
        return [i for i in self.invoke['response']['qr_trades'] if i['qr_id'] == self.qr_id]['status']

    def GetTid(self):
        """根据qr_id查询tid，如果tradelist长度为0说明未扫码"""
        tradelist = [i for i in self.invoke['response']['qr_trades'] if i['qr_id'] == self.qr_id]
        if len(tradelist) == 0:
            return 0
        else:
            return tradelist[0]['tid']


class Query(BaseHandler):
    """根据传入的qr_id获取详情"""

    def post(self, *args, **kwargs):
        qr_id = self.get_argument('qr_id')
        info = Judge(qr_id).JudgePay()
        self.write(json.dumps(info))
