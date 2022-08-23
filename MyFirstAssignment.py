# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
First assignment: find sum of first 100

"""

import numpy as np
list100 = np.linspace(1, 100, 100, dtype =int)
sum100 = sum(list100)
print('sum of first 100 intergers is: {}'.format(sum100))

otherSum=0
for i in range(101):
    otherSum += i

print( 'otherSum = {}'.format(otherSum))        
