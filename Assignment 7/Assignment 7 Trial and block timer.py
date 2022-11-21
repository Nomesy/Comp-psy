# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:32:10 2022

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

nBlocks = 2
nTrials = 3 

block_Timer = core.Clock()
trial_Timer = core.Clock()
    
stim_timer = core.Clock()


#=====================
        #START TRIAL
        #===================== 
    
for block in range(nBlocks):
    block_Timer.reset()
    for trial in range(nTrials): 
            my_image.image = os.path.join(image_dir,stims[trial])
            trial_Timer.reset()
            #-draw fixation
            fix_text = visual.TextStim(win, text='+')
            fix_text.draw()
            #-flip window
            win.flip()
            #-wait time (stimulus duration)
            core.wait(2)
            
            #-draw image
            clock_wait_timer.reset()
            while clock_wait_timer.getTime() <= 2: 
                #-draw image
                my_image.draw()
                #-flip window
                win.flip()
                #-wait time (stimulus duration)
            print('Stimuli '+str(trial)+' time =', clock_wait_timer.getTime())
            
             #-draw end trial text
            end_trial_msg = "end of trial"
            end_trial_text = visual.TextStim(win, text=end_trial_msg)
            end_trial_text.color = 'green'
            end_trial_text.draw()
            #-flip window
            win.flip() 
            #-wait time (stimulus duration)
            core.wait(2)
            print('Trial '+str(trial)+' total time =', trial_Timer.getTime())
    print('Block '+str(block)+' total time =', block_Timer.getTime())
win.close()