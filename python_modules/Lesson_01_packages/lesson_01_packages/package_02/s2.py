# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 07:28:21 2019

@author: Ben
"""

from package_02.s2_params import param1

class Sub2:  

    param2 = 'YELLOW UNICORN'
    
    def __init__(self):
        pass
        
    def run_sub2(self):
        print('"{}" is an import, whilst "{}" is a param internal to Sub2 class'.format(param1,self.param2))