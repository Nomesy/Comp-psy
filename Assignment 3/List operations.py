# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:44:24 2022

@author: Morsr
"""
import numpy as np
#1
numlist = [1,2,3]
print(numlist)
print(numlist * 2)

#2
numarray = np.array([1,2,3])
print(numarray)
print(numarray * 2)

#3
strlist = ['do','re', 'mi','fa']

#['dodo','rere','mimi','fafa']
print([strlist[0],strlist[1]*2,strlist[2]*2,strlist[3]*2])
#['do','re','mi','fa','do','re','mi','fa']
print(strlist * 2)
#['do','do','re','re','mi','mi','fa','fa']
print([strlist[0],strlist[0],
       strlist[1],strlist[1],
       strlist[2],strlist[2],
       strlist[3],strlist[3]])
#[['do','do'],['re','re'],['mi','mi'],['fa','fa']]
print([[strlist[0],strlist[0]],
       [strlist[1],strlist[1]],
       [strlist[2],strlist[2]],
       [strlist[3],strlist[3]]])


