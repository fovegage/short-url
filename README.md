<div align="center">

## 三分钟搭建你的个人支付接口

**基于有赞云支付和有赞微小店实现个人收款支付接口解决方案 .**

[![Build Status](https://travis-ci.org/thundernet8/YouzanPayPortal.svg?branch=master)](https://travis-ci.org/thundernet8/YouzanPayPortal)
[![GitHub license](https://img.shields.io/github/license/thundernet8/YouzanPayPortal.svg)](https://github.com/thundernet8/YouzanPayPortal/blob/master/LICENSE)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

</div>

<br>

## 介绍

基于有赞云支付和有赞微小店实现个人收款解决方案, 提供如下两个服务:

- 基于Tornado和有赞云支付接口综合开发
- 代理简化生成收款二维码的 API，支持微信支付宝扫描付款
- 你只需传入out_trade_no、total_fee、subject、body即可得到payid
- 根据返回的payid即可发起支付，支付完成后，页面自动跳转自预先配置的url
- 接收有赞云的交易消息推送并处理(需要二次请求交易详情)，简化订单状态通知到指定的服务器



## 有赞云注册及创建应用

* 注册[有赞云](https://console.youzanyun.com/register) 开发者

* 创建[有赞微小店](https://h5.youzan.com/v2/index/wxdpc) 并扫码下载相应 APP 便于后续管理资金，注意这个小店在有赞后台看不到，只有 APP 可见

* 应用授权-有赞云控制台创建自用型应用并授权刚创建的店铺，在[推送服务]设置中设置推送网址*http://www.example.com/notice* , 同时勾选下方的交易消息选项。


## 项目配置

### 有赞云支付配置

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

### url配置

```
# 支付成功返回网址
url = ''
```

### MongoDB配置

- 若安装过程中出现问题, 请Google或Issues
- MongoDB安装请参考[Linux平台安装MongoDB](http://www.runoob.com/mongodb/mongodb-linux-install.html)


### Nginx配置
* 提供公网服务，请使用 Nginx 代理至 Tornado，这样能够让有赞推送消息到达推送网址
* Nginx安装，请参考[Nginx 安装配置](http://www.runoob.com/linux/nginx-install-setup.html)




