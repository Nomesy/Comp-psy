# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:00:11 2022

@author: Morsr
"""

#1
sub_code = 'sub'
subnr_int = 2
subnr_str = '2'

#print(sub_code + subnr_int)
print(sub_code + subnr_str)

#sub 2
print(sub_code + '' + subnr_str)

#sub 222
print(sub_code + " " + subnr_str + subnr_str + subnr_str)

#sub2sub2sub2
print((sub_code + subnr_str)*3)

#subsubsub222
print(sub_code + sub_code + sub_code + subnr_str + subnr_str + subnr_str)