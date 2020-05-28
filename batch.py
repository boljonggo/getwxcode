#!/usr/bin/python3
# -*- coding: utf-8 -*-
import openpyxl, sys, requests, json, time, datetime, os, pathlib

# 读取token
def readToken():
    f = open("access_token.txt","r")
    # 将txt文件的所有内容读入到字符串str中
    access_token = f.read()
    print(access_token)
    # 关闭文件
    f.close()
    return access_token

# access_token = '33_cwUFIwvydlqZadUa3803oStE_As_0xgpB3tvLcHbyPmQmIKV1FdDmUkHUCRGoqcS85tWMF4PBa4GmnOc-IFcLoimsJxzxUYfkVlme89GBnt3JUneHU6CHIRVTKKV7_YB7iq0VJHmMOVF3SqpEQVbAHAZLQ'

# 加载excel
def loadExcel(fileName):
    wb = openpyxl.load_workbook(fileName)
    table = wb.get_sheet_by_name(wb.sheetnames[0])

    # 循环遍历
    list = []
    for row in table.rows:
        temp = []
        for cell in row:
            temp.append(cell.value)
            # print(cell.value)
        list.append(temp)
    print(list)
    return list

# 生成目录
def createDir(folderName):
    now_time = datetime.datetime.now()
    now_date = now_time.strftime('%Y%m%d')
    # path = 'image/'+folderName+'/'+now_date
    path = 'image/'+folderName
    my_file = pathlib.Path(path)
    if my_file.exists() == False:
        os.makedirs(path)
    return path

# ###########################################################################
# 获取小程序码
def getwxcode(list, access_token, path):
    storeName = list[1]
    pathStr = list[2]
    url = 'https://api.weixin.qq.com/wxa/getwxacode?access_token='+access_token
    body = {
        "path": pathStr,
        "width": "1280px",
        "is_hyaline": True
        }

    res = requests.post(url, data = json.dumps(body))

    msg = ''
    if res.status_code == 200:
        msg = '--成功--'+storeName
    else:
        msg = '--失败--'+storeName

    # 保存文件
    fileName = storeName+'.png'
    with open(path+'/'+fileName, 'wb')as png:
        png.write(res.content)
    return msg

if __name__ == "__main__":
    access_token = readToken()
    list = loadExcel('list.xlsx')
    path = createDir('门店直播列表小程序码')
    # 循环遍历excel数据，获取小程序码
    for item in list:
        msg = getwxcode(item, access_token, path)
        print(msg)
