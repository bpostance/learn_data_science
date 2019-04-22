# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 07:28:00 2019

@author: Ben
"""
from package_01 import p1
from package_01.subpackage_1a import constants
from package_02 import p2

p1.Package01.run_package01()

print('THis is Pi={}. A parameter from package_01.subpackage_1a\n'.format(constants.pi))

new = p2.Package02()
new.run_package_02()