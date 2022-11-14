# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 09:00:55 2022

@author: Morsr
"""
from psychopy import gui, core, visual, monitors, event
from datetime import datetime
import os
import numpy as np

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
exp_info = { 'subject_nr':0,
            'age':0,
            'handedness':('right','left', 'ambi'),
            'gender': '',
            'session': 1}
#setup the dictionary for the gui

                          
print(exp_info)

print("All variables have been created! Now ready")

my_dlg = gui.DlgFromDict(dictionary=exp_info, title="subject info",fixed=['session'],order=['session', 'subject_nr','age', 'gender', 'handedness'])

if exp_info['subject_nr'] ==0: #nothing entered
    #create another dialog box (not from a dictionary because we're just showing an error message)
    err_dlg = gui.Dlg(title='error message') #give the dlg a title
    err_dlg.addText('Enter a valid subject number!') #create an error message
    err_dlg.show() #show the dlg
    core.quit() #quit the experiment
    
#make sure subject can consent to taking part in the experiment        
if exp_info['age'] < 18:
    err_dlg = gui.Dlg(title='error message')
    err_dlg.addText('%d year olds cannot give consent!' % (exp_info['age']))
    err_dlg.show()
    core.quit()


#get date and time
date=datetime.now()
print(date)
exp_info['date'] = (str(date.hour) + '-' +
                    str(date.day) + '-' +
                    str(date.month) + '-' +
                    str(date.year))
print(exp_info['date'])


#-create a unique filename for the data
filename = str(exp_info['subject_nr']) + '-' + str(exp_info['date']) + '.csv'
main_dir = os.getcwd()
sub_dir = os.path.join(main_dir,'sub_info', filename)




#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=20, distance=60)
mon.setSizePix([1920,1080])
mon.save()
thisSize = mon.getSizePix()
thisWidth = thisSize[0]
thisHeight = thisSize[1]

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, units='pix', size=[1920,1080], color=[-1,-1,-1], colorSpace='rgb')


#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define experiment start text unsing psychopy functions
start_msg = 'Welcome to my experiment!'
#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue to the next block"
#-define stimuli using psychopy functions (images, fixation cross)
image_dir = os.path.join(main_dir,'images')
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg']
my_image = visual.ImageStim(win, units='pix', size=(400,400))
fix_text = visual.TextStim(win,text='+')
nBlocks = 2
nTrials = 4


#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_text = visual.TextStim(win, text=start_msg)
start_text.draw()
win.flip() 

#-allow participant to begin experiment with button press
event.waitKeys() 



#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for Block in range(nBlocks):
    #-present block start message
    block_text = visual.TextStim(win, text=block_msg)
    block_text.draw()
    win.flip() 
    event.waitKeys() 
    
    #-randomize order of trials here
    np.random.shuffle(stims)
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    horizMult = [-1,1,1,-1]
    vertMult = [1,1,-1,-1]
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        my_image.image = os.path.join(image_dir,stims[trial])
        my_image.pos = (horizMult[trial]*thisWidth/4, vertMult[trial]*thisHeight/4)
       
        #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys()
        
        #-draw image
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys()
        
        #-draw end trial text
        end_trial_msg = "end of trial"
        end_trial_text = visual.TextStim(win, text=end_trial_msg)
        end_trial_text.color = 'aquamarine'
        end_trial_text.draw()

        #-flip window
        win.flip() 
        #-wait time (stimulus duration)
        event.waitKeys() 
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()