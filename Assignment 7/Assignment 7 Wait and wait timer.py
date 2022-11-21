# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 20:48:26 2022

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

wait_timer = core.Clock() #define a clock
    

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
        wait_timer.reset()
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(2) #instead of 2 seconds core.wait was actually about 2.016 (2.014-2.018) seconds on average.
        wait_timer.getTime()
        print('Stimuli '+str(trial)+' time =', wait_timer.getTime())
        
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