# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 23:54:23 2022

@author: Morsr
"""

from psychopy import core, event, visual, monitors

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

nTrials=10
my_text=visual.TextStim(win)
fix=visual.TextStim(win, text='+')
sub_resp = [[-1]*nTrials]

#event.clearEvents() #this only clears key presses that happen right before the trails begin so they are only cleared in the trail when the 

for trial in range(nTrials):
    
    keys = event.getKeys(keyList=['1','2']) #put getkeys HERE
    my_text.text = "trial %i" %trial #insert integer into the string with %i
    
    fix.draw()
    win.flip()
    core.wait(2)
    
    event.clearEvents() #this allows the code to be able to clear any key presses that happen right before the stimulus is presented per trial.
    
    my_text.draw()
    win.flip()
    core.wait(1)
    
    print("keys that were pressed", keys) #which keys were pressed?
    
    if keys:
        sub_resp = keys[0] #only take first response
        
    print("response that was counted", sub_resp)    
    
win.close()