# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 07:28:21 2019

@author: Ben
"""

from package_02.p2_params import param1

class Package02:  

    param2 = 'YELLOW UNICORN'
    
    def __init__(self):
        pass
        
    def run_package_02(self):
        print('"{}" is an import, whilst "{}" is a param internal to Package_02 class\n'.format(param1,self.param2))