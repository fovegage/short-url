### 有赞云支付Python实现

#### 三分钟搭建你的个人支付接口

- 基于Tornado和有赞云支付接口综合开发
- 你只需传入out_trade_no、total_fee、subject、body即可得到payid

#### 有赞云支付配置

- 主目录下修改settings, 申请有赞云支付账号后依次填入client_id、client_secret、kdt_id
- 请不要修改grant_type配置项
```
youzan = {
    'client_id': '有赞云id',
    'client_secret': '有赞云密钥',
    'grant_type': 'silent',  # 请勿修改
    'kdt_id': '店铺id'
}
```

#### MongoDB配置

- MongoDB安装请参考[Linux平台安装MongoDB](http://www.runoob.com/mongodb/mongodb-linux-install.html)
- 若安装过程中出现问题, 请Google或Issues

