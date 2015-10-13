#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年10月10日

@author: ruixidong
'''
from DataAccess.Handler import RedisCli
from common import utility
import time,json
def exists(code):
    return RedisCli.hexists("Q2k:Codes", code)

def apply(url,bites,hours):
    md5=utility.md5code(url)
    RedisCli.hset("Q2k:Urls:%s"%md5,"state",0)
    RedisCli.rpush("Q2k:Queue:Apply",json.dumps(dict(url=url,bites=bites,hours=hours)))

def get_apply_url():
    s=RedisCli.lpop("Q2k:Queue:Apply")
    if s!=None:
        return json.loads(s)    

def get_code(url):
    md5=utility.md5code(url)
    data = RedisCli.hgetall("Q2k:Urls:%s"%md5)
    data["state"] = int(data["state"])
    return data

def get_url(code):
    return RedisCli.hget("Q2k:Codes",code)


def regist_url(url,bites=8,hours=48):
    
    md5=utility.md5code(url)
    
    cinfo = dict(state=0,code="",url=url,expire=0)
    cinfo.update(RedisCli.hgetall("Q2k:Urls:%s"%md5))
    if cinfo["state"]=="0":
        if cinfo["code"]=="":
            while True:
                code = utility.generateCode(bites)
                if not exists(code):
                    break
                time.sleep(0.1)
            cinfo["code"]=code
         
    
        RedisCli.hset("Q2k:Codes", cinfo["code"],url)
        RedisCli.hset("Q2k:Urls:%s"%md5,"code",cinfo["code"])
        RedisCli.hset("Q2k:Urls:%s"%md5,"state",1)
    
    #默认将过期时间向后延期
    RedisCli.hset("Q2k:Urls:%s"%md5,"expire",time.time()+hours*60*60)
    return cinfo["code"]
    