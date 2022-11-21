# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:41:17 2021

@author: Youmu
"""
from fastapi import FastAPI
import uvicorn
import nest_asyncio
import requests
import ssl
import  json
from pydantic import BaseModel
from sport.jump import ropeSkipping
from sport.yangwoqizuo import situps
from sport.fuwocheng import fuwocheng
from sport.kaihetiao import kaihetiao
from sport.shendun import shendun
from sport.jianbudun import jianbudun

ssl._create_default_https_context = ssl._create_unverified_context
nest_asyncio.apply()
app = FastAPI()


class Item(BaseModel):
    videopath: str = None
    id: str = None
    cut: str = None


# 跳绳
@app.post('/tiaoSheng')
def tiaoSheng(information: Item):
    cid = information.id
    ccut = information.cut
    count = ropeSkipping(information.videopath)
    payload = {'id': cid, 'cut': ccut, 'result':count}
    data_json = json.dumps(payload)
    r = requests.post('https://sports.qdszgh.cn/app/api/match/updateResult', data=data_json,headers={'Content-Type': 'application/json', "Accept": "*/*"})
    print(data_json)
    print(r)
    return count


# 仰卧起坐
@app.post('/yangWoQiZuo')
def yangWoQiZuo(information: Item):
    cid = information.id
    ccut = information.cut
    count = situps(information.videopath)
    payload = {'id': cid, 'cut': ccut, 'result':count}
    data_json = json.dumps(payload)
    r = requests.post('https://sports.qdszgh.cn/app/api/match/updateResult', data=data_json,headers={'Content-Type': 'application/json', "Accept": "*/*"})
    print(data_json)
    print(r)
    return count


# 俯卧撑
@app.post('/fuWoCheng')
def fuWoCheng(information: Item):
    cid = information.id
    ccut = information.cut
    count = fuwocheng(information.videopath)
    payload = {'id': cid, 'cut': ccut, 'result':count}
    data_json = json.dumps(payload)
    r = requests.post('https://sports.qdszgh.cn/app/api/match/updateResult', data=data_json,headers={'Content-Type': 'application/json', "Accept": "*/*"})
    print(data_json)
    print(r)
    return count
   


# 开合跳
@app.post('/kaiHeTiao')
def kaiHeTiao(information: Item):
    cid = information.id
    ccut = information.cut
    count = kaihetiao(information.videopath)
    #print('*******************************')
    #print(information.videopath)
    #print('*******************************')
    payload = {'id': cid, 'cut': ccut, 'result':count}
    data_json = json.dumps(payload)
    r = requests.post('https://sports.qdszgh.cn/app/api/match/updateResult', data=data_json,headers={'Content-Type': 'application/json', "Accept": "*/*"})
    #print('*******************************')
    print(data_json)
    print(r)
    #print('*******************************')
    return count


# 深蹲
@app.post('/shenDun')
def shenDun(information: Item):
    cid = information.id
    ccut = information.cut
    count = shendun(information.videopath)
    payload = {'id': cid, 'cut': ccut, 'result':count}
    data_json = json.dumps(payload)
    r = requests.post('https://sports.qdszgh.cn/app/api/match/updateResult', data=data_json,headers={'Content-Type': 'application/json', "Accept": "*/*"})
    print(data_json)
    print(r)
    return count


# 箭步蹲
@app.post('/jianBuDun')
def jianBuDun(information: Item):
    cid = information.id
    ccut = information.cut
    count = jianbudun(information.videopath)
    payload = {'id': cid, 'cut': ccut, 'result':count}
    data_json = json.dumps(payload)
    r = requests.post('https://sports.qdszgh.cn/app/api/match/updateResult', data=data_json,headers={'Content-Type': 'application/json', "Accept": "*/*"})
    print(data_json)
    print(r)
    return count


if __name__ == "__main__":
    try:
        uvicorn.run(app=app,
                    host="0.0.0.0",
                    port=3004,
                    workers=1)
        print('web服务启动成功，端口为3004')
    except:
        raise RuntimeError('web服务启动失败！')
