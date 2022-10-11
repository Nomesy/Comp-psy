# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 11:01:09 2022

@author: Morsr
"""

#1
iteration = 0

while iteration < 20:
    if iteration < 10:
        print('%i, image1.png' %iteration)
        
    elif iteration < 20:
        print('%i, image2.png' %iteration)
    iteration = iteration + 1
    
#2
import random
response = ''
looping = True
failsafe = 0
while looping:
    response = random.randint(0,10)
    print(response)
    print('this is an image')
    failsafe = failsafe + 1
    
    if response == 1 or response == 2 or failsafe == 5:
        looping = False
        
        
