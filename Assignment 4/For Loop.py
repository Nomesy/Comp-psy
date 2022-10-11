# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:04:26 2022

@author: Morsr
"""
#1 and #2
myname = 'Kyle'

counter = -1
for letter in myname:
    counter = counter + 1
    print(letter)
    print(counter)
    
#3 and #4
names = ['Amy', 'Rory', 'River']


for name in names:
    print(name)
    lettercounter = -1
    for letter in name:
        lettercounter = lettercounter + 1
        print(letter)
        print(lettercounter)
    
