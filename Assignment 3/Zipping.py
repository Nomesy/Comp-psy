# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 10:01:13 2022

@author: Morsr
"""

import numpy as np
first_item = []
second_item = []
imgs_F = ['face1.png']*5 + ['face2.png']*5 + ['face3.png']*5 + ['face4.png']*5+  ['face5.png']*5
        
imgs_H = ['house1.png']*5 + ['house2.png']*5 + ['house3.png']*5 + ['house4.png']*5+ ['house5.png']*5
        
first_item.extend(imgs_F)
first_item.extend(imgs_H)
first_item.extend(imgs_F)
first_item.extend(imgs_H)
print(first_item)
print(len(first_item))


imgs_H = ['face1.png','face2.png',
            'face3.png','face4.png',
            'face5']*5
imgs_H = ['house1.png','house2.png',
            'house3.png','house4.png',
            'house5']*5

second_item.extend(imgs_H)
second_item.extend(imgs_F)
second_item.extend(imgs_H)
second_item.extend(imgs_F)
print(second_item)
print(len(second_item))
        
cues = ['cue1']*50 + ['cue2']*50

catimgs = list(zip(first_item,second_item,cues))
print(catimgs)

np.random.shuffle(catimgs)

print(catimgs)