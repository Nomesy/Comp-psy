# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:12:11 2022

@author: Morsr
"""

#1
import numpy as np
import matplotlib.pyplot as plt
mixnums = np.array([1,2.0,3,4.0,5,6.0])
print(mixnums)
#2
mixtypes = np.array([1,2.0,3,4.0,'5','6.0'])
print(mixtypes)
#3
oddarray = np.arange(1,100,2)
print(oddarray)
#4

logarray = np.logspace(1,5,16)
print(logarray)

plt.plot(logarray)
plt.show
plt.pause(100)






