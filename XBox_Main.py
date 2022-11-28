import psychopy
from psychopy import core, visual, gui, data
import pygame, time, ctypes
import numpy as np
from numpy.random import random
from psychopy.hardware import keyboard

# Make a text file to save data
expInfo = {"subject": "0"}
dlg = gui.DlgFromDict(expInfo, title="Two-armed bandit task XBOX")
fileName = "XBox_rumblePress_" + expInfo["subject"] + "_" + data.getDateStr()
dataFile = open(
    fileName + ".csv", "w"
)  # a simple text file with 'comma-separated-values'
dataFile.write("subject, block_type, block, condition, trial, right_offer, left_offer, offer_right_image, offer_left_image, exp_value_right, exp_value_left, exp_value_chosen, choice_location, choice_key, choice_card, unchosen_card, chosen_card_image, unchosen_card_image, rt, randomwalk_counter, exp_value1, exp_value2, exp_value3, exp_value4, reward\n")
subjectN = expInfo["subject"]
# choise_key = 1 -> left, choice_key = 2 -> right
##Initializing game
pygame.init()
clock = pygame.time.Clock()
keepPlaying = True
j = pygame.joystick.Joystick(0)
j.init()

# aborting the experiment if escape is pressed
def abort(window):
    # check keyboard presses
    kb = keyboard.Keyboard()
    kb.start()
    keys = kb.getKeys(["escape"])
    if "escape" in keys:
        window.close()
        core.quit()
# create a window
win = visual.Window( [800, 600], fullscr = True, monitor="testMonitor", units="deg", color=(-1, -1, -1), useFBO=False)
mytimer = core.Clock()

# Number of trials and Stimuli Pictures
from random import sample
n = 5 # Number of trials
stim_id = np.zeros(n)
won = visual.ImageStim(win, image="rw.png", pos=[0, 0], size=4)
lost = visual.ImageStim(win, image="ur.jpg", pos=[0, 0], size=4)
fixation = visual.TextStim(win, text="+", pos=[0, 0], color=(0, 0, 0))

# Random Walks for 200 Trials - Two Different random walks used to counterbalance
RW = np.zeros((12,50))
# Counterbalance
x = (int(subjectN))%4
deckList = [ ["1.jpg","2.jpg","3.jpg","4.jpg"], ["5.jpg","6.jpg","7.jpg","8.jpg"], ["9.jpg","10.jpg","11.jpg","12.jpg"] ]
picList = sample(deckList, 3)
# RandomWalk1 - rwCntr = 1  
if (x == 0 or x == 1):
    rwCntr = 1
    RW[0] = RW[4] = RW[8] = [0.511076546,0.517796443,0.498939688,0.498193315,0.472267853,0.48900464,0.498922937,0.523305174,0.538202722,0.538742055,0.576408806,0.58170588,0.578706679,0.542007718,0.51169699,0.513158928,0.513426935,0.505704724,0.504573157,0.511492418,0.512951285,0.539572991,0.56095771,0.575401102,0.541014126,0.536918816,0.541079589,0.559641612,0.566867971,0.562069061,0.557017169,0.587964414,0.569423526,0.56834307,0.599079702,0.614921267,0.628075493,0.631242143,0.600609567,0.598478627,0.60144404,0.630195312,0.628568645,0.636994371,0.650015763,0.626001871,0.606772055,0.609756275,0.606158462,0.585330427]
    RW[1] = RW[5] = RW[9] = [0.615232533,0.631199867,0.626315633,0.609226527,0.620106582,0.609411022,0.661106815,0.661043011,0.617130773,0.61305354,0.627053837,0.6084257,0.597368238,0.603047222,0.59667375,0.577589974,0.585694186,0.54789599,0.582335652,0.588279021,0.553509108,0.552815737,0.535255398,0.524393705,0.532040408,0.511692898,0.54671574,0.570750529,0.54476025,0.559260499,0.570453061,0.562455492,0.583546956,0.565200904,0.567372701,0.558903517,0.545721743,0.538071442,0.562917382,0.574174471,0.580661228,0.582970551,0.572586617,0.565568304,0.5781911,0.554193525,0.585886385,0.601875425,0.595767883,0.596690297]
    RW[2] = RW[6] = RW[10] = [0.413504079,0.375335495,0.374984468,0.371343772,0.35386843,0.353156918,0.351148204,0.385479761,0.38403906,0.400369013,0.389573429,0.368726719,0.375355878,0.38842331,0.398928367,0.371810296,0.379887863,0.373664559,0.369915918,0.34718102,0.365459609,0.364821817,0.373035803,0.364677663,0.39083719,0.371897574,0.389383809,0.408417182,0.383885215,0.406860111,0.389734908,0.364845558,0.38651511,0.411760625,0.404213812,0.380656038,0.352549374,0.347063514,0.341152187,0.340254534,0.358175358,0.366861123,0.357029746,0.384631609,0.386636695,0.376640317,0.329837755,0.322472207,0.298351175,0.304980312]
    RW[3] = RW[7] = RW[11] = [0.466504194,0.47234587,0.491193418,0.486122834,0.463675252,0.444784776,0.459669582,0.445975487,0.477824508,0.494179332,0.442060048,0.429884006,0.451621205,0.453322749,0.449059956,0.445080478,0.422775713,0.418810463,0.404711898,0.429775493,0.420212923,0.410726764,0.376882621,0.358107826,0.373729847,0.398780507,0.405865749,0.403418308,0.398536524,0.407780991,0.40633374,0.430319959,0.469700007,0.45608609,0.497188985,0.476236411,0.509842719,0.530542784,0.525341883,0.519319672,0.531828439,0.522351056,0.532129282,0.54344664,0.52618086,0.575008411,0.546233567,0.544792119,0.559135463,0.528689445] 
# RandomWalk2 - rwCntr = 2
elif (x == 2 or x == 3):
    rwCntr = 2
    RW[0] = RW[4] = RW[8] = [0.167787674,0.176264347,0.206677553,0.216551625,0.21991786,0.209090036,0.215508938,0.219868403,0.223820368,0.25320591,0.272116099,0.234286576,0.209829698,0.194746258,0.254919143,0.268446939,0.260713561,0.273570125,0.269452755,0.268741649,0.289598518,0.299460569,0.275422902,0.266650787,0.254259812,0.251503025,0.260664603,0.254900351,0.270226286,0.231605059,0.233739069,0.24432205,0.193554899,0.204964705,0.22048214,0.211101934,0.219326053,0.221341547,0.214118114,0.217505069,0.249081937,0.255981224,0.288213763,0.294374293,0.308994906,0.289973458,0.29306391,0.292135198,0.293886334,0.304272396]
    RW[1] = RW[5] = RW[9] = [0.332201416,0.355471562,0.3490424,0.358181966,0.364707579,0.3895513,0.39060737,0.430440014,0.4539861,0.485995524,0.489357893,0.484630844,0.493007884,0.496165246,0.498060855,0.473753497,0.427927548,0.42862063,0.435371131,0.425551488,0.44190032,0.419525056,0.397611772,0.379139537,0.383103254,0.426705428,0.434578853,0.456535155,0.431125609,0.434793002,0.473135831,0.452508743,0.458621481,0.43001655,0.429045935,0.447650766,0.456165741,0.433155402,0.447660961,0.447456341,0.458162882,0.480978505,0.511556199,0.530811847,0.512913286,0.533187647,0.537872242,0.523160461,0.527646571,0.548355336]
    RW[2] = RW[6] = RW[10] = [0.584847675,0.582595424,0.578794293,0.569745321,0.582527891,0.587455063,0.582464681,0.545053358,0.530883085,0.507816291,0.494989907,0.446302549,0.441292304,0.424090899,0.410741903,0.384469806,0.397409959,0.380302803,0.39026973,0.408454439,0.404768464,0.422610309,0.408863932,0.405854252,0.425425396,0.44409494,0.476699219,0.471375184,0.45401501,0.441888062,0.456731037,0.406064085,0.401876712,0.409321444,0.424862287,0.423948221,0.43257228,0.4363313,0.408906602,0.40122215,0.382054645,0.383924023,0.401205729,0.350203513,0.336134109,0.325220477,0.357892701,0.408168742,0.394241012,0.386662209]
    RW[3] = RW[7] = RW[11] = [0.302670058,0.290755999,0.275426328,0.268568422,0.302042001,0.336540119,0.363378709,0.369794555,0.365747455,0.36426522,0.378430477,0.406276663,0.408056555,0.411853134,0.425420016,0.434571537,0.467037886,0.458160423,0.413401572,0.410963982,0.423231262,0.389718337,0.39059245,0.398445672,0.3844496,0.389570929,0.351861927,0.358204472,0.360838495,0.36725969,0.401609609,0.393803515,0.402704902,0.416668377,0.419699964,0.428911523,0.39910528,0.390289699,0.411267062,0.401024283,0.370374616,0.368787043,0.38383929,0.362927966,0.367033206,0.368488345,0.34679011,0.356952705,0.356189797,0.348042517] 

################################
#####    Rumble Feature    #####
################################

# Define necessary structures
class XINPUT_VIBRATION(ctypes.Structure):
    _fields_ = [("wLeftMotorSpeed", ctypes.c_ushort),
                ("wRightMotorSpeed", ctypes.c_ushort)]
xinput = ctypes.windll.xinput1_4  # Load Xinput.dll
# Set up function argument types and return type
XInputSetState = xinput.XInputSetState
XInputSetState.argtypes = [ctypes.c_uint, ctypes.POINTER(XINPUT_VIBRATION)]
XInputSetState.restype = ctypes.c_uint
# A helper function:
def set_vibration(controller, left_motor, right_motor):
    vibration = XINPUT_VIBRATION(int(left_motor * 65535), int(right_motor * 65535))
    XInputSetState(controller, ctypes.byref(vibration))


# Experiment Flow Function    
def main():
    instructionsPhase = False
    trainPhase = False
    quizPhase = False
    gamePhase = True
    
    # Start Instruction Phase
    if instructionsPhase:
        instructionsFunc()
        # Changing Phase to Test\Quiz Phase
        instructionsPhase = False
        quizPhase = True
        trainPhase = False
        gamePhase = False
    
    # Start Test\Quiz Phase
    if quizPhase:
        testFunc()
        # Changing Phase to Training Phase
        instructionsPhase = False
        quizPhase = False
        trainPhase = True
        gamePhase = False

    if trainPhase:
        training1 = visual.ImageStim(win, image="training1.jpg",  units='norm', size=[2,2], interpolate = True)
        training1.draw()
        win.update()
        while True:
            events = pygame.event.poll()
            if (events.type == pygame.JOYBUTTONDOWN):
                #Event 4 -> Pressing down left button, Event 5 -> Pressing down right button
                if events.button == 5:
                    # Changing Phase to Game Phase
                    instructionsPhase = False
                    quizPhase = False
                    trainPhase = False
                    gamePhase = True
                    break
    if gamePhase:
        blockCnt = 0
        # Counterbalance block order
        possibleOrder = [ [0,1,2], [0,2,1], [1,2,0], [1,0,2], [2,0,1], [2,1,0] ]
        indx = int(subjectN) % 6
        # 0 -> vibration during choice
        # 1 -> vibration during outcome
        # 2 -> vibration off
        for x in possibleOrder[indx]:
            if (x == 0):
                rumbleCond = "press"
                blockCnt = blockCnt + 1
                rumbleTraining = visual.ImageStim(win, image="rumbleTraining.jpg",  units='norm', size=[2,2], interpolate = True)
                rumbleTraining.draw()
                win.update()
                # Start Practice Block
                while True:
                    events = pygame.event.poll()
                    if (events.type == pygame.JOYBUTTONDOWN):
                        #Event 5 -> Pressing down right button
                        if events.button == 5:
                            mainExperimentModes(dataFile, blockCnt, subjectN, win, rumbleCond, 5, 'practice', 0)
                            break
                endPractice = visual.ImageStim(win, image="endPractice.jpg",  units='norm', size=[2,2], interpolate = True)
                endPractice.draw()
                win.update()
                while True:
                    events = pygame.event.poll()
                    if (events.type == pygame.JOYBUTTONDOWN):
                        #Event 5 -> Pressing down right button
                        if events.button == 5:
                            break
                endBlock = "endblock" + str(blockCnt) + ".jpg"
                start = visual.ImageStim(win, image="startRumbleBlock.jpg",  units='norm', size=[2,2], interpolate = True)
                end = visual.ImageStim(win, image=endBlock,  units='norm', size=[2,2], interpolate = True)
                start.draw()
                win.update()
                while True:
                    events = pygame.event.poll()
                    # Wait for response to begin block
                    if (events.type == pygame.JOYBUTTONDOWN):
                    #Event 4 -> Pressing down left button, Event 5 -> Pressing down right button
                        if events.button == 5:
                            mainExperimentModes(dataFile, blockCnt, subjectN, win, rumbleCond, n, 'test', 0)
                            break
                end.draw()
                win.update()
                # Wait for response to end block
                while True:
                    events = pygame.event.poll()
                    if (events.type == pygame.JOYBUTTONDOWN):
                    #Event 4 -> Pressing down left button, Event 5 -> Pressing down right button
                        if events.button == 5:
                            break
            if (x == 1):
                blockCnt = blockCnt + 1
                rumbleCond = "reward" 
                rumbleTraining = visual.ImageStim(win, image="rumbleTraining.jpg",  units='norm', size=[2,2], interpolate = True)
                rumbleTraining.draw()
                win.update()
                while True:
                    events = pygame.event.poll()
                    if (events.type == pygame.JOYBUTTONDOWN):
                        #Event 4 -> Pressing down left button, Event 5 -> Pressing down right button
                        if events.button == 5:
                            mainExperimentModes(dataFile, blockCnt, subjectN, win, rumbleCond, 5, 'practice', 1)
                            break
                endPractice = visual.ImageStim(win, image="endPractice.jpg",  units='norm', size=[2,2], interpolate = True)
                endPractice.draw()
                win.update()
                while True:
                    events = pygame.event.poll()
                    if (events.type == pygame.JOYBUTTONDOWN):
                        #Event 5 -> Pressing down right button
                        if events.button == 5:
                            break
                endBlock = "endblock" + str(blockCnt) + ".jpg"
                start = visual.ImageStim(win, image="startRumbleBlock.jpg",  units='norm', size=[2,2], interpolate = True)
                end = visual.ImageStim(win, image=endBlock,  units='norm', size=[2,2], interpolate = True)
                start.draw()
                win.update()
                # Wait for response to begin block
                while True:
                    events = pygame.event.poll()
                    if (events.type == pygame.JOYBUTTONDOWN):
                    #Event 4 -> Pressing down left button, Event 5 -> Pressing down right button
                        if events.button == 5:          
                            mainExperimentModes(dataFile, blockCnt, subjectN, win, rumbleCond, n, 'test', 1)
                            break
                end.draw()
                win.update()
                # Wait for response to end block
                while True:
                    events = pygame.event.poll()
                    if (events.type == pygame.JOYBUTTONDOWN):
                    #Event 5 -> Pressed Right Button
                        if events.button == 5:
                            break
            if (x == 2):
                blockCnt = blockCnt + 1
                rumbleCond = "none"
                regularTraining = visual.ImageStim(win, image="regularTraining.jpg",  units='norm', size=[2,2], interpolate = True)
                regularTraining.draw()
                win.update()
                while True:
                    events = pygame.event.poll()
                    if (events.type == pygame.JOYBUTTONDOWN):
                        #Event 5 -> Pressed Right Button 
                        if events.button == 5:
                            mainExperimentModes(dataFile, blockCnt, subjectN, win, rumbleCond, 5, 'practice', 2)
                            break
                endPractice = visual.ImageStim(win, image="endPractice.jpg",  units='norm', size=[2,2], interpolate = True)
                endPractice.draw()
                win.update()
                while True:
                    events = pygame.event.poll()
                    if (events.type == pygame.JOYBUTTONDOWN):
                        #Event 5 -> Pressing down right button
                        if events.button == 5:
                            break
                endBlock = "endblock" + str(blockCnt) + ".jpg"
                start = visual.ImageStim(win, image="startRegularBlock.jpg",  units='norm', size=[2,2], interpolate = True)
                end = visual.ImageStim(win, image=endBlock,  units='norm', size=[2,2], interpolate = True)
                start.draw()
                win.update()
                # Wait for response to begin block
                while True:
                    events = pygame.event.poll()
                    if (events.type == pygame.JOYBUTTONDOWN):
                    #Event 4 -> Pressing down left button, Event 5 -> Pressing down right button
                        if events.button == 5:
                            mainExperimentModes(dataFile, blockCnt, subjectN, win, rumbleCond, n, 'test', 2)
                            break
                end.draw()
                win.update()
                # Wait for response to end block
                while True:
                    events = pygame.event.poll()
                    if (events.type == pygame.JOYBUTTONDOWN):
                    #Event 4 -> Pressing down left button, Event 5 -> Pressing down right button
                        if events.button == 5:
                            break


# # # # # # #
# Functions #
# # # # # # #

def WrongAnswerFunc():
    mistake = visual.ImageStim(win, image="mistake.jpg",  units='norm', size=[2,2], interpolate = True)    
    mistake.draw()
    win.update()
    while True:
        events = pygame.event.poll()
        if (events.type == pygame.JOYBUTTONDOWN):
            # Pressed A for "Try Again"
            if (events.button == 0):
                break
            elif (events.button == 1):
                instructionsFunc()
                break

def instructionsFunc():
    currSlide = 1
    while currSlide < 14:
        slideName = "Slide" + str(currSlide) + ".jpg"
        slidePic = visual.ImageStim(win, image=slideName,  units='norm', size=[2,2], interpolate = True)
        slidePic.draw()
        win.update()
        while True:
            events = pygame.event.poll()
            if (events.type == pygame.JOYBUTTONDOWN):
                #Event 4 -> Pressing down left button, Event 5 -> Pressing down right button
                if events.button == 5:
                    currSlide = currSlide + 1
                    break
                if (events.button == 4 and currSlide > 1) :
                    currSlide = currSlide - 1
                    break

def testFunc():
    nTest = 1
    while nTest < 9:
        slideName = "test" + str(nTest) + ".jpg"
        testPic = visual.ImageStim(win, image=slideName,  units='norm', size=[2,2], interpolate = True)
        testPic.draw()
        win.update()
        while True:
            events = pygame.event.poll()
            if (events.type == pygame.JOYBUTTONDOWN):
                # Question 1
                if nTest == 1:
                    # Correct Answer Case
                    # Event 1 -> Pressed B Button
                    if events.button == 1:
                        nTest = nTest + 1
                        break
                    # Wrong Answer Case
                    # Event 0 -> Pressed A Button
                    # Event 2 -> Pressed X Button
                    elif (events.button == 0) or (events.button == 2):
                        WrongAnswerFunc()
                        # set nTest = 1 to start quiz from the start 
                        nTest = 1
                        break    
                
                # Question 2
                if nTest == 2:
                    # Correct Answer Case
                    # Event 0 -> Pressed A Button
                    if events.button == 0:
                        nTest = nTest + 1
                        break
                    # Wrong Answer Case
                    # Event 1 -> Pressed B Button
                    # Event 2 -> Pressed X Button
                    elif (events.button == 1) or (events.button == 2):
                        WrongAnswerFunc()
                        # set nTest = 1 to start quiz from the start 
                        nTest = 1                        
                        break 
                
                # Question 3
                if nTest == 3:
                    # Correct Answer Case
                    # Event 1 -> Pressed B Button
                    if events.button == 1:
                        nTest = nTest + 1
                        break
                    # Wrong Answer Case
                    # Event 0 -> Pressed A Button
                    elif (events.button == 0):
                        WrongAnswerFunc()
                        # set nTest = 1 to start quiz from the start 
                        nTest = 1                        
                        break

                # Question 4
                if nTest == 4:
                    # Correct Answer Case
                    # Event 0 -> Pressed A Button
                    if events.button == 0:
                        nTest = nTest + 1
                        break
                    # Wrong Answer Case
                    # Event 1 -> Pressed B Button
                    elif (events.button == 1):
                        WrongAnswerFunc()
                        # set nTest = 1 to start quiz from the start 
                        nTest = 1                        
                        break

                # Question 5
                if nTest == 5:
                    # Correct Answer Case
                    # Event 1 -> Pressed B Button
                    if events.button == 1:
                        nTest = nTest + 1
                        break
                    # Wrong Answer Case
                    # Event 0 -> Pressed A Button
                    elif (events.button == 0):
                        WrongAnswerFunc()
                        # set nTest = 1 to start quiz from the start 
                        nTest = 1                        
                        break

                # Question 6
                if nTest == 6:
                    # Correct Answer Case
                    # Event 2 -> Pressed X Button
                    if events.button == 2:
                        nTest = nTest + 1
                        break
                    # Wrong Answer Case
                    # Event 0 -> Pressed A Button
                    # Event 1 -> Pressed B Button
                    elif (events.button == 0) or (events.button == 1):
                        WrongAnswerFunc()
                        # set nTest = 1 to start quiz from the start 
                        nTest = 1                        
                        break

                # Question 7
                if nTest == 7:
                    # Correct Answer Case
                    # Event 1 -> Pressed B Button
                    if events.button == 1:
                        nTest = nTest + 1
                        break
                    # Wrong Answer Case
                    # Event 0 -> Pressed A Button
                    elif (events.button == 0):
                        WrongAnswerFunc()
                        # set nTest = 1 to start quiz from the start 
                        nTest = 1                        
                        break
                
                # Question 8
                if nTest == 8:
                    # Correct Answer Case
                    # Event 2 -> Pressed X Button
                    if events.button == 2:
                        nTest = nTest + 1
                        break
                    # Wrong Answer Case
                    # Event 0 -> Pressed A Button
                    # Event 1 -> Pressed B Button
                    elif (events.button == 0) or (events.button == 1):
                        WrongAnswerFunc()
                        # set nTest = 1 to start quiz from the start 
                        nTest = 1                        
                        break

def mainExperimentModes(dataFile, blockCnt, subjectN, win, rumbleCond, trials, blockType, deckIndx):
    # Block Condition: 
    if (rumbleCond == "press"):
        cond = "vibration during choice"
    elif (rumbleCond == "reward"):
        cond = "vibration during outcome"
    elif (rumbleCond == "none"):
        cond = "vibration off"
    # Initilizing Game
    pygame.init()
    clock = pygame.time.Clock()
    j = pygame.joystick.Joystick(0)
    j.init()
    for t in range(1, trials+1):
        abort(win)
        RTwarning = False
        mytimer = core.Clock()
        # Draw the stimuli and update the window
        pictures = sample(picList[deckIndx], 2)
        for i in range(1,5):
            if i==1:
                card1=picList[deckIndx][0]
            if i==2:
                card2=picList[deckIndx][1]
            if i==3:
                card3=picList[deckIndx][2]
            if i==4:
                card4=picList[deckIndx][3]
        unpresented_cards = []
        for card in picList[deckIndx]:
            if card not in pictures:
                unpresented_cards.append(card)
        card1_prob = RW[int(card1.split(".")[0])-1][t-1]
        card2_prob = RW[int(card2.split(".")[0])-1][t-1]
        card3_prob = RW[int(card3.split(".")[0])-1][t-1]
        card4_prob = RW[int(card4.split(".")[0])-1][t-1]
        btnL = visual.ImageStim(win, image=pictures[0], pos=[-6, 0], size=(5,8))
        btnR = visual.ImageStim(win, image=pictures[1], pos=[6, 0], size=(5,8))
        fixation.draw()
        win.update()
        core.wait(1)
        #core.wait(0.3)
        fixation.draw()
        btnL.draw()
        btnR.draw()
        win.update()
        mytimer.reset(0)
        while True:
            if (mytimer.getTime() > 6 and RTwarning == False):
                rt_warning = visual.ImageStim(win, image="RTWarning.jpg",  units='norm', size=[2,2], interpolate = True)
                rt_warning.draw()
                win.update()
                while True:
                    events = pygame.event.poll()
                    if (events.type == pygame.JOYBUTTONDOWN):
                        if (events.button == 5):
                            RTwarning = True
                            break
            events = pygame.event.poll()
            if (events.type == pygame.JOYBUTTONDOWN):
                #Event 4 -> Pressing down left button, Event 5 -> Pressing down right button
                if events.button == 4:
                    RT = str(mytimer.getTime())
                    btnL.draw()
                    fixation.draw()
                    stim_id = int(pictures[0].split(".")[0])
                    other_id = int(pictures[1].split(".")[0])
                    stim_id_deck = (stim_id)%4
                    other_id_deck = (other_id)%4
                    if (stim_id_deck == 0):
                        stim_id_deck = 4
                    elif (other_id_deck ==0):
                        other_id_deck = 4
                    prob1 = RW[other_id-1][t-1]
                    prob2 = RW[stim_id-1][t-1]
                    key = 1
                    stimapr = "left"
                    dataFile.write("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," 
                        % (
                            subjectN,
                            blockType,
                            blockCnt,
                            cond,
                            t,
                            str(other_id_deck),
                            str(stim_id_deck),
                            pictures[1],
                            pictures[0],
                            prob1,
                            prob2,
                            prob2,
                            stimapr,
                            key,
                            str(stim_id_deck),
                            str(other_id_deck),
                            pictures[0],
                            pictures[1],
                            RT,
                            rwCntr,
                            card1_prob,
                            card2_prob, 
                            card3_prob, 
                            card4_prob,
                        )
                    )
                    if (rumbleCond == "press"):
                        # Rumble feedback
                        win.update()
                        set_vibration(0, 1, 1)
                        time.sleep(0.5)
                        set_vibration(0, 0, 0)
                        core.wait(0.25)
                    else: 
                        win.update()
                        core.wait(0.75)
                    break
                elif events.button == 5:
                    RT = str(mytimer.getTime())
                    btnR.draw()
                    fixation.draw()
                    stim_id = int(pictures[1].split(".")[0])
                    other_id = int(pictures[0].split(".")[0])
                    stim_id_deck = (stim_id)%4
                    other_id_deck = (other_id)%4
                    if (stim_id_deck == 0):
                        stim_id_deck = 4
                    elif (other_id_deck ==0):
                        other_id_deck = 4
                    prob1 = RW[stim_id-1][t-1]
                    prob2 = RW[other_id-1][t-1]
                    key = 2
                    stimapr = "right"
                    dataFile.write("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," 
                        % (
                            subjectN,
                            blockType,
                            blockCnt,
                            cond,
                            t,
                            str(stim_id_deck),
                            str(other_id_deck),
                            pictures[1],
                            pictures[0],
                            prob1,
                            prob2,
                            prob1,
                            stimapr,
                            key,
                            str(stim_id_deck),
                            str(other_id_deck),
                            pictures[1],
                            pictures[0],
                            RT,
                            rwCntr,
                            card1_prob,
                            card2_prob, 
                            card3_prob, 
                            card4_prob,
                        )
                    )       
                    if (rumbleCond == "press"):
                        # Rumble feedback
                        win.update()
                        set_vibration(0, 1, 1)
                        time.sleep(0.5)
                        set_vibration(0, 0, 0)
                        core.wait(0.25)
                    else: 
                        win.update()
                        core.wait(0.75)
                    break           
    
        ##########################################
        # outcome using Random Walk for n trials #
        ##########################################
        curr_prob = RW[stim_id-1][t-1]
        if (random() < curr_prob):
            won.draw()
            dataFile.write("%i\n" % (1,))
        else:
            lost.draw()
            dataFile.write("%i,\n" % (0,))
        if (rumbleCond == "reward"):
                        # Rumble feedback
                        win.update()
                        set_vibration(0, 1, 1)
                        time.sleep(0.5)
                        set_vibration(0, 0, 0)
                        core.wait(0.25)
        else: 
            win.update()
            core.wait(0.75)

main()

