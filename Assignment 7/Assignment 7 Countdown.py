# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 22:42:11 2022

@author: Morsr
"""

from psychopy import visual, monitors, event, core

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

import os
#stuff you only have to define once at the top of your script
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

my_image = visual.ImageStim(win)

stims = ['face01.jpg','face02.jpg','face03.jpg']
nTrials=3 

countdown_timer = core.CountdownTimer() #define a clock
    

#=====================
        #START TRIAL
#===================== 
for trial in range(nTrials): 
    my_image.image = os.path.join(image_dir,stims[trial])
    
    #-draw fixation
    fix_text = visual.TextStim(win, text='+')
    fix_text.draw()
    #-flip window
    win.flip()
    #-wait time (stimulus duration)
    core.wait(2)
        
    #-draw image
    countdown_timer.reset()
    countdown_timer.add(2)
    imgStartTime = countdown_timer.getTime()
    while countdown_timer.getTime() >0: 
        #-draw image
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
    imgEndTime = countdown_timer.getTime()
    print('Stimuli '+str(trial)+' time =', (imgStartTime - imgEndTime))
        
    #-draw end trial text
    end_trial_msg = "end of trial"
    end_trial_text = visual.TextStim(win, text=end_trial_msg)
    end_trial_text.color = 'green'
    end_trial_text.draw()

    #-flip window
    win.flip() 
     #-wait time (stimulus duration)
    core.wait(2)
        
win.close()
