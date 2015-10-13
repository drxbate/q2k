#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年7月22日

@author: ruixidong
'''
import sys
reload(sys)

setdefaultencoding = getattr(sys, "setdefaultencoding")

if setdefaultencoding:
    setdefaultencoding("utf8") 

#init flask app ---begin
    
from flask import Flask, g, request,Response,url_for,redirect
import os

from flask.ext.bootstrap import Bootstrap
from common import cacheManager,Settings

Settings.setOptions(configFile="setting")

app = Flask(__name__,template_folder="_templates",static_folder="_static")
app.config['SECRET_KEY'] = '123456'
app.debug = True


bootstrap = Bootstrap(app)
cacheManager.init_cache(app)

#init flask app ---end

#load http modules for flask app --begin
from httpModules import extjs,homePage

app.register_blueprint(homePage,url_prefix= "/")
app.register_blueprint(extjs,url_prefix= "/js")
#app.jinja_env.add_extension('jinja2.ext.i18n')

#load http modules for flask app --end

def run():
    print "run httpd"
    app.run(host="0.0.0.0",port=9910,debug=True)
    
    
if __name__=="__main__":
    run()