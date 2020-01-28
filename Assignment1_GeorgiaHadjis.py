#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:35:54 2020

@author: georgiahadjis
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %% import packages

import numpy as np
import pandas as pd
import os
import sys
import random
import csv
from psychopy import visual, core, event, gui, logging

# %% add a key to press to terminate the experiment
event.globalKeys.add(key='q', func=core.quit)

# %% use gui to collect information about subject ID and session number

# create a gui object
subgui = gui.Dlg()

# add fields for subject ID and session number
subgui.addField("Subject ID:")
subgui.addField("SessionNumber:")

# show the gui
subgui.show()

# put the inputted data in easy to use variables
subjID = subgui.data[0]
sessNum = subgui.data[1]

# %% prepare output

#making sure subject ID and session number haven't already been run
outputFileName = 'data' + os.sep + 'sub' + subjID + 'sessNum' + sessNum + '.csv'
if os.path.isfile(outputFileName):
    sys.exit("data for this session already exists")

#making output dataframe to store results
outVars = ['subj', 'condition', 'trial', 'letter','response', 'rt',
           'stimOn', 'stimDur', 'corr_responses']
out = pd.DataFrame(columns=outVars)

# experiment parameters
stimDur = 1
respDur = 2
isiDur = 1
#importing predetermined files with blocks of trials
block1 = pd.read_csv('block1.csv')
block2 = pd.read_csv('block2.csv')
block3 = pd.read_csv('block3.csv')
block4 = pd.read_csv('block4.csv')
blocks = [block1, block2, block3, block4] #create a list with each of the blocks to randomly select from
random.shuffle(blocks)

#looping through the list of blocks and generating a dataframe for the randomly selected block file
for b in range(4):
    b_df = blocks[b]
    b_df1 = pd.DataFrame(b_df)

# %% Setting up window

win = visual.Window(size=[800, 800], fullscr=True,
                    allowGUI=False, color=('black'), units='height')


# ensuring screen refresh rate is what it should be
win.recordFrameIntervals = True
win.refreshThreshold = 1 / 60 + 0.005
logging.console.setLevel(logging.WARNING)


# %% Presenting an image

# Instructions
instr = visual.ImageStim(win, image="instructions1.png",
                         units = 'norm', size = 1.5, interpolate=False)
# be sure to use the full/relative path to the image location on your computer
# if you set your window units to "height" size=1 means full screen height
# setting interpolate to True will make images look nicer but could add time

# draw image to window buffer
instr.draw()
# flip window to reveal image
win.flip()
keys = event.waitKeys()

instr2 = visual.ImageStim(
    win, image="instructions2.png", units = 'norm', size = 1.5, interpolate=False)
# draw image to window buffer
instr2.draw()
# flip window to reveal image
win.flip()
keys = event.waitKeys()

instr3 = visual.ImageStim(
    win, image="instructions3.png", units = 'norm', size = 1.5, interpolate=False)
# draw image to window buffer
instr3.draw()
# flip window to reveal image
win.flip()
keys = event.waitKeys()

instr_keys = visual.ImageStim(
    win, image="instructions_keypress.png", units = 'norm', size = 1.5, interpolate=False)
# draw image to window buffer
instr_keys.draw()
# flip window to reveal image
win.flip()
keys = event.waitKeys()

instr4 = visual.ImageStim(
    win, image="instructions4.png", units = 'norm', size = 1.5, interpolate=False)
# draw image to window buffer
instr4.draw()
# flip window to reveal image
win.flip()
keys = event.waitKeys()

instr5 = visual.ImageStim(
    win, image="instructions5.png", units = 'norm', size = 1.5, interpolate=False)
# draw image to window buffer
instr5.draw()
# flip window to reveal image
win.flip()
keys = event.waitKeys()

instr6 = visual.ImageStim(
    win, image="instructions6.png", units = 'norm', size = 1.5, interpolate=False)
# draw image to window buffer
instr6.draw()
# flip window to reveal image
win.flip()
keys = event.waitKeys()

instr7 = visual.ImageStim(
    win, image="instructions7.png", units = 'norm', size = 2, interpolate=False)
# draw image to window buffer
instr7.draw()
# flip window to reveal image
win.flip()
keys = event.waitKeys()

get_ready = visual.ImageStim(
    win, image="Get_Ready.png", units = 'norm', size = 1.5, interpolate=False)
# draw image to window buffer
get_ready.draw()
# flip window to reveal image
win.flip()
keys = event.waitKeys(maxWait=2)

"""Start Experiment!"""

#making visual stimuli
corText = visual.TextStim(win, text='correct', pos=(0, 0), height=0.05) 
incText = visual.TextStim(win, text='incorrect', pos=(0, 0), height=0.05) 
fixationText = visual.TextStim(win, text="+", color='white', pos=(0, 0),
                               height=0.05)

#setting up basic timing functions
expClock = core.Clock()
trialClock = core.Clock()
stimClock = core.Clock()
respClock = core.Clock()

for i in range(len(b_df1)):
    letters = b_df1.loc[i, 'letters'] #defining letters as each value in column 'letters' of dataframe
    corr_responses = b_df1.loc[i,'corr_responses'] #defining correct responses with each value in column of correct responses in dataframe
    out.loc[i,'subj'] = subjID  # record subject in output file
    out.loc[i, 'letter'] = letters
    out.loc[i,'corr_responses'] = corr_responses # record correct responses in output file
    #defining four strings for the four condition types
    baseline_pain = 'baseline_pain'
    pain = 'pain'
    baseline_elec = 'baseline_elec'
    elec = 'elec'
    sn = int(sessNum) #converting session number from gui into an integer
    #determining based on subject ID and session number which condition will be inputted into the output dataframe
    if int(subjID) % 2 == 1:
        if sn == 1:
            out.loc[i,'condition'] = baseline_pain
        elif sn == 2:
            out.loc[i,'condition'] = pain
        elif sn == 3:
            out.loc[i,'condition'] = baseline_elec
        elif sn == 4:
            out.loc[i,'condition'] = elec
    else:
        if sn == 1:
            out.loc[i,'condition'] = baseline_elec
        elif sn == 2:
            out.loc[i,'condition'] = elec
        elif sn == 3:
            out.loc[i,'condition'] = baseline_pain
        elif sn == 4:
            out.loc[i,'condition'] = pain
    trialClock.reset()

    thisStim = visual.ImageStim(win, image='/Users/moayedilab/Documents/PSY1210/Assignment1/Images/' + letters, pos=(0, 0))

    thisStim.draw()

    while trialClock.getTime() < isiDur: #ensuring that trial is not prematurely presented during interstimulus interval
        core.wait(.001)

    win.flip()
    stimClock.reset()
    respClock.reset()

    out.loc[i, 'stimOn'] = expClock.getTime() #record when trials are presented

    trialResp = 0
    trialRT = 0
    event.clearEvents()
    while respClock.getTime() < respDur: 
        # check if showing stimulus
        if stimClock.getTime() < stimDur:
            thisStim.draw()
            win.flip()
        else:
            win.flip()
            if np.isnan(out.loc[i, 'stimDur']):  # record when stimulus removed
               out.loc[i, 'stimDur'] = expClock.getTime() - out.loc[i, 'stimOn'] #record stimulus duration

        # check for a key response
        keys = event.getKeys(keyList=['f', 'j'], timeStamped=respClock)
        if len(keys) > 0:  # if response made, collect response information
            trialResp, trialRT = keys[-1]
    if trialResp == corr_responses: #displaying accuracy as trial-by-trial-feedback
        # save for summary at end: np.mean(out.correct)
        out.loc[i, 'correct'] = 1
        corText.draw()
    else:
        out.loc[i, 'correct'] = 0
        incText.draw()
    rt = visual.TextStim(
        win, text=f"rt: {trialRT:.3f} s", color='white', pos=(0, -.1),
         height=0.05) #display reaction time after each trial
    rt.draw()
    win.flip()
    core.wait(1)
    fixationText.draw()
    win.flip()
    # record trial parameters
    out.loc[i, 'trial'] = i
    out.loc[i, 'stimDur'] = expClock.getTime() - out.loc[i, 'stimOn']
    # save responses if made
    if trialResp is not None:
        out.loc[i, 'response'] = trialResp
        out.loc[i, 'rt'] = trialRT
    else:
        out.loc[i, 'response'] = None
        out.loc[i, 'rt'] = None

#making rating scales
PainScale = visual.RatingScale(
    win, choices=['yes', 'no'],
    markerStart=0.5, respKeys=(['f', 'j']), maxTime= 10, noMouse=True, pos = (0,-0.25))
Pain_text = visual.TextStim(
        win, text="Was the stimulus on your leg painful?", color='white', pos=(0, 0.1), height=0.05)
IntensityScale = visual.RatingScale(win, low=0, high=10, maxTime= 10, marker='circle',
    tickMarks=[0,1,2,3,4,5,6,7,8,9,10],markerStart=0,markerColor='white', leftKeys = 'left', rightKeys = 'right', noMouse=True, scale = '0 = not intense, 10 = most intense imagineable', pos = (0, -0.25))
Intensity_text = visual.TextStim(
        win, text="How intense was the stimulus on your leg?", color='white', pos=(0, 0.1),
         height=0.05)
SalienceScale = visual.RatingScale(win, low=0, high=10, maxTime= 10, marker='circle',
    tickMarks=[0,1,2,3,4,5,6,7,8,9,10],markerStart=0,markerColor='white', leftKeys = 'left', rightKeys = 'right', noMouse=True, scale ='0 = not salient, 10 = extremely salient', pos = (0, -0.25))
Salience_text = visual.TextStim(
        win, text="How salient was the stimulus on your leg?", color='white', pos=(0, 0.1),
         height=0.05)

PainScale.reset()
while PainScale.noResponse: # before the response is made
    PainScale.draw()
    Pain_text.draw()
    win.flip()

Pain_Rating = PainScale.getRating()

IntensityScale.reset()
while IntensityScale.noResponse: # before the response is made
    IntensityScale.draw()
    Intensity_text.draw()
    win.flip()

Intensity_Rating = IntensityScale.getRating()

SalienceScale.reset()
while SalienceScale.noResponse: # before the response is made
    SalienceScale.draw()
    Salience_text.draw()
    win.flip()

Salience_Rating = SalienceScale.getRating()

#save rating responses into output file
out.loc[i, 'pain_rating'] = Pain_Rating
out.loc[i, 'intensity_rating'] = Intensity_Rating
out.loc[i, 'salience_rating'] = Salience_Rating

# showing summary data at the end of the block
avg_accuracy = (np.mean(out.loc[:,'correct']))*100
print(avg_accuracy)
avg_rt = np.mean(out.loc[:,'rt'])
print(avg_rt)
avg_accuracy_text = visual.TextStim(win, text=f"Average Accuracy: {avg_accuracy:.0f}%", color='white', pos=(0, 0), height=0.05)
avg_rt_text = visual.TextStim(win, text=f"Average RT: {avg_rt:.3f} s", color='white', pos=(0, -.1), height=0.05)
avg_accuracy_text.draw()
avg_rt_text.draw()
win.flip()
core.wait(3)

# manage output
out.to_csv(outputFileName, index=False)

win.close()
core.quit()
