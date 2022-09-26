# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 10:13:23 2022

@author: Morsr
"""
#1
print(1 == 1.0)
print("1" == "1.0")
#2
print(5 == (3+2))
#3
print(1 == 1.0 or "1" == "1.0" and 5 == (3+2))
print(1 == 1.0 and not "1" == "1.0" or 5 == (3+2))
print(1 == 1.0 or "1" == "1.0" or 5 == (3+2))
print(1 == 1.0 or "1" == "1.0" and not 5 == (3+2))
print(1 == 1.0 and not "1" == "1.0" and 5 == (3+2))