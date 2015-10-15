#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
from flask import Blueprint,redirect,render_template,request,Response
from flask_httpauth import HTTPBasicAuth


import json
from common import Settings

admin = Blueprint("admin",__name__)

auth = HTTPBasicAuth()

@admin.route("")
@admin.route("/index.html")
@admin.route("/index1.html")
@auth.login_required
def __root__():
    return "ok"

@auth.verify_password
def verify_password(username, password):
    if username=="admin" and password=="admin":
        return True
    else:
        return False