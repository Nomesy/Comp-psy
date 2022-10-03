# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:07:02 2022

@author: Morsr
"""

#1
list100 = list(range(101))
print(list100)

#2
print(list100[:10])

#3
temp = list100[1::2]
print(temp[::-1])

#4
temp = list100[-4:-1]
print(temp[::-1])

#5

print(list100[39:44])
print(list100[39:44] == [39,40,41,42,43])