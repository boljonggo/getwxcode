#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests, sys, json, time

# 1.获取 access_token
# 访问地址
host="https://api.weixin.qq.com/cgi-bin/token"
# 参数
params = {'grant_type': 'client_credential', 'appid': '填写小程序的appid', 'secret': '填写小程序的AppSecret'}

r = requests.get(host, params=params)

print(r.json())
print('过期时间 = ' + str(r.json()['expires_in']))
print('access_token = '+r.json()['access_token'])
access_token = r.json()['access_token']