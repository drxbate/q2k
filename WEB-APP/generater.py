#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年10月10日

@author: ruixidong
'''

from ObjectModules import QrCodeModule
import time
from common import Settings
def generate():
    
    while True:
        QrCodeModule.QrCodeGenerate.generateOne()
        time.sleep(0.1)

if __name__ == '__main__':
    generate()