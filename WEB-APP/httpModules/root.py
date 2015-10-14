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

homePage = Blueprint("app",__name__)

@homePage.route("")
def __root__():
    return redirect("_/index.html")

@homePage.route("<regex('[a-zA-Z0-9]{6}':code>")
def __tourl__(code):
    qrc=QrCodeModule.QrCode()
    uinfo = qrc.geturl(code)
    url=uinfo["url"]
    return redirect(url)

@homePage.route("_/index.html")
def __homePage__():
    return render_template("generate_code.html")

@homePage.route("_/login.html")
def __profile__():
    return render_template("login.html")

@homePage.route("_/generate", methods=["POST"])
def __generate__():
    url = request.form.get("url")
    qrc=QrCodeModule.QrCode()
    qrc.apply(url, bites=6, hours=72)
    return json.dumps(dict(state=0)) 

@homePage.route("_/state", methods=["GET"])
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
    
