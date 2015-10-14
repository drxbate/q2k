#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Blueprint,redirect,render_template,request,Response
import json
from ObjectModules import QrCodeModule as qB
from ObjectModules import QrCodeModule
from common import Settings

api = Blueprint("api",__name__)

@api.route("/generate", methods=["POST"])
def __generate__():         
    url = request.form.get("url")
    qrc=QrCodeModule.QrCode()
    qrc.apply(url, bites=6, hours=72)
    return json.dumps(dict(state=0)) 

@api.route("/state", methods=["GET"])
def __state__():
    url = request.args.get("url")
    qrc=QrCodeModule.QrCode()
    try:
        cdata = qrc.getcode(url)
        src="%s/%s.png"%(Settings.output.baseurl,cdata["code"])
        return json.dumps(dict(state=0,data=cdata,src=src))
    except QrCodeModule.CodeNotGeneratedException,cnge:
        return json.dumps(dict(state=cnge.code,error=cnge.message))
    except QrCodeModule.QrCodeException,qce:
        return json.dumps(dict(state=qce.code,error=qce.message,data=qce.data))
    
