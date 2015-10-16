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
from werkzeug.routing import BaseConverter

Settings.setOptions(configFile="setting")

class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        self.map = map
        self.regex = args[0]

app = Flask(__name__,template_folder="_templates",static_folder="_static")
app.config['SECRET_KEY'] = '123456'
app.url_map.converters['regex'] = RegexConverter
app.debug = True



bootstrap = Bootstrap(app)
app.extensions["bootstrap"]["cdns"]["bootstrap"].fallback.baseurl="//cdn.bootcss.com/bootstrap/3.3.5/"
app.extensions["bootstrap"]["cdns"]["jquery"].fallback.baseurl="//cdn.bootcss.com/jquery/1.11.3/"

cacheManager.init_cache(app)

#init flask app ---end

#load http modules for flask app --begin
from httpModules import extjs,homePage,api,admin

app.register_blueprint(homePage,url_prefix= "/")
app.register_blueprint(api,url_prefix= "/api")
app.register_blueprint(extjs,url_prefix= "/js")
app.register_blueprint(admin,url_prefix= "/admin")
#app.jinja_env.add_extension('jinja2.ext.i18n')

#load http modules for flask app --end

def run():
    print "run httpd"
    app.run(host="0.0.0.0",port=9910,debug=True)
    
    
if __name__=="__main__":
    run()