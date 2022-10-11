# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:57:37 2022

@author: Morsr
"""
response = '1'
#1
if response == '1' or response == '2':
    if response == '1':
        print('correct')
        
    if response == '2':
        print('incorrect')
    
    
elif response == 'NaN':
        print('subject did not respond')
        
else:
    print('subject pressed the wrong key')
    
    
#2 it does exactly as its suppost to, reports back 'correct' with '1', 'incorrect' with '2', and 'subject pressed the wrong key' with '4'.
