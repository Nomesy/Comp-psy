# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:34:10 2022

@author: Morsr
"""
#this can output various information about your experiment
from psychopy import visual, monitors, event, core, logging
import os
#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

#set durations
fix_dur = 2 #200 ms
stim_dur = 2 #100 ms
text_dur = 2 #200 ms


refresh = 1.0/60.0
#set frame counts
fix_frames = int(fix_dur / refresh) #whole number
stim_frames = int(stim_dur / refresh) #whole number
text_frames = int(text_dur / refresh) #whole number
#the total number of frames to be presented on a trial
total_frames = int(fix_frames + stim_frames + text_frames)

fix = visual.TextStim(win, text='+')



nBlocks=2
nTrials=4


#add information to record dropped frames
win.recordFrameIntervals = True #record frames
#give the monitor refresh rate plus a few ms tolerance (usually 4ms)
win.refreshThreshold = 1.0/60.0 + 0.004

# Set the log module to report warnings to the standard output window 
#(default is errors only).
logging.console.setLevel(logging.WARNING)


main_dir = os.getcwd()
image_dir = os.path.join(main_dir,'images')
my_image = visual.ImageStim(win)
stims = ['face01.jpg','face02.jpg','face03.jpg', 'face04.jpg']



block_Timer = core.Clock()
trial_Timer = core.Clock()
stim_Timer = core.Clock()



for block in range(nBlocks):
    block_Timer.reset()
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        trial_Timer.reset()
        my_image.image = os.path.join(image_dir,stims[trial])
        #=====================
        #START TRIAL
        #=====================   
        for frameN in range(total_frames): 
            #-draw stimulus
            if 0 <= frameN <= fix_frames:     
                fix.draw()
                win.flip()
                    
            #number of frames for image after fixation
            if fix_frames < frameN <= (fix_frames+stim_frames):      
                my_image.draw()
                win.flip()   
            #number of frames for the final text stimulus    
            if (fix_frames+stim_frames) < frameN < total_frames:  
                 end_trial_msg = "end of trial"
                 end_trial_text = visual.TextStim(win, text=end_trial_msg)
                 end_trial_text.color = 'green'
                 end_trial_text.draw()
                 win.flip()  
                 

        #this will print total number of frames dropped following every trial
        print('Overall, %i frames were dropped.' % win.nDroppedFrames)
        # dropped frames are ussually under 6 so keeping the frame method.
        print('Trial '+str(trial)+' total time =', trial_Timer.getTime())
        
    print('Block '+str(block)+' total time =', block_Timer.getTime())

win.close()