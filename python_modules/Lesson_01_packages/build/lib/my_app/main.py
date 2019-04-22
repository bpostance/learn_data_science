# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 07:28:00 2019

@author: Ben
"""

import sys
sys.path.insert(0, 'C:/Users/Ben/Desktop/app/sub1')
sys.path.insert(0, 'C:/Users/Ben/Desktop/app/sub2')

from sub1 import s1
from sub2 import s2

s1.Sub1.run_sub1()

new = s2.Sub2()
new.run_sub2()