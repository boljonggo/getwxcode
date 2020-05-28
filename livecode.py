#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests, sys, json, time, datetime, os, pathlib

#设置文件对象
f = open("access_token.txt","r")
#将txt文件的所有内容读入到字符串str中
access_token = f.read()
print(access_token)
#关闭文件
f.close()

# 要生成的页面的路径
pathStr = "plugin-private://wx2b03c6e691cd7370/pages/live-player-plugin"

url = 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token='+access_token
body = {
    "path": pathStr,
    "scene": "room_id=58",
    "width": "1280px",
    "is_hyaline": True
}

res = requests.post(url, data = json.dumps(body))
print(res.status_code)
msg = ''
if res.status_code == 200:
    msg = '--成功--生成小程序码'
else:
    msg = '--失败--生成小程序码'
print(msg)

fileName = '平台首页.png'
now_time = datetime.datetime.now()
now_date = now_time.strftime('%Y%m%d')
path = 'image/test/'+now_date
my_file = pathlib.Path(path)
if my_file.exists() == False:
    os.makedirs(path)

with open(path+'/'+fileName, 'wb')as png:
    png.write(res.content)
