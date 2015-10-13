#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年10月10日

@author: ruixidong
'''

from DataAccess import QrCode as QrCodeHandler

import time

class QrCodeException(Exception):
    code,message=-1,"Error"
    def __init__(self):
        Exception.__init__(self)

    
class UrlNotExistsException(QrCodeException):
    code,message=-2,"UrlNotExists"

class ExpireException(QrCodeException):
    code,message=1,"Expire"    
    def __init__(self,data):
        QrCodeException.__init__(self)
        self.data=data


class CodeNotGeneratedException(QrCodeException):
    code,message=2,"CodeNotGenerated"


class QrCode:
    def getcode(self,url):
        cinfo = QrCodeHandler.get_code(url)
        if cinfo==None:
            raise UrlNotExistsException()
        
        cinfo.update(dict(url=url))
        t = time.time()
        if cinfo["state"]==0:
            raise CodeNotGeneratedException()
        if cinfo["expire"]<t:
            raise ExpireException(cinfo)
        return cinfo
    def geturl(self,code):
        url = QrCodeHandler.get_url(code)
        return self.getcode(url)

    def apply(self,url,bites=8,hours=72):
        QrCodeHandler.apply(url,bites,hours)

class QrCodeGenerate:
    @classmethod
    def generateOne(cls):
        import qrcode
        from common import Settings
        info = QrCodeHandler.get_apply_url()
        if info!=None:
            code = QrCodeHandler.regist_url(info["url"],info["bites"],info["hours"])
            url = "%s/%s"%(Settings.output.outsurl,code)
            qr = qrcode.QRCode(     
                version=1,     
                error_correction=qrcode.constants.ERROR_CORRECT_L,     
                box_size=10,     
                border=4, 
            ) 
            qr.add_data(url) 
            qr.make(fit=True)  
            img = qr.make_image()
            
            img.save('%s/%s.png'%(Settings.output.path,code))
        
    