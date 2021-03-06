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

homePage = Blueprint("root",__name__)
 
@homePage.route("<regex('[a-zA-Z0-9]{6}'):code>")
def __tourl__(code):
    qrc=QrCodeModule.QrCode()
    uinfo = qrc.geturl(code)
    url=uinfo["url"]
    return redirect(url)

@homePage.route("")
@homePage.route("index.html")
def __homePage__():
    return render_template("generate_code.html")


@homePage.route("login.html")
def __profile__():
    return render_template("login.html")

@homePage.route("googleb81a9db8331cbc53.html")
def __google_valid_file__():
    return "google-site-verification: googleb81a9db8331cbc53.html"