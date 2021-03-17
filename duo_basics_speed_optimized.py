#!/usr/bin/env python
# duo_basics.py - completes German Basics 1 a specified number of times
#not very dynamic tbh

import pyautogui, time, re, random

#clipboard functionality
import tkinter as tk
root = tk.Tk()
root.withdraw()

#TO DO ################# Count number of questions for perfect looping
#and no checking in between each one

def next():
    #removed unfinished checking
    pyautogui.click(1457, 782, duration=0.2)
    time.sleep(.1)
    #removed error checking
    pyautogui.click()
    return

def find_click(image):
    if str(image) != 'None':
        temp = pyautogui.locateOnScreen(image)
        if str(temp) != 'None':
            temp = pyautogui.center(temp)
            pyautogui.click(temp, duration=0.2)
    else:
        return -1
    return 0

def braille(x1, h1, x2, h2, parse):
    #select and copy the phrase to translate
    pyautogui.moveTo(x1, h1, duration=0.2)
    pyautogui.dragTo(x2, h2, duration=0.2)
    pyautogui.hotkey('ctrl', 'c')
    phrase = root.clipboard_get()
    if parse == True:
        #take out the horrible weird duolingo specific whitespace
        phrase = re.sub('[^A-Za-z ]', '', phrase)
        phrase = phrase.lower()
    return phrase

print('Welcome to your very own Duo doer.')
print('This program is not currently very dynamic.')
print('Please ensure that duolingo is in a chrome tab on the right half of the screen.')
print('Remember to not let anything obscure the duolingo window.')
rep = int(input('How many iterations would you like to perform?\n'))

try:
    while rep > 0:
        rep = rep - 1 #Loop for as many times as user specifies
        print('Use Ctrl+C with this window in focus to stop at any time.')
        #wait for the page to load
        time.sleep(5)
        find_click('practice_again.png')
        time.sleep(5)
        find_click('start_practice.png')
        time.sleep(1)
        #which button is there?
        # again_loc = pyautogui.locateOnScreen('practice_again.png')
        # if str(again_loc) != 'None': #practice again is present
        #     again_loc = pyautogui.center(again_loc)
        #     pyautogui.click(again_loc, duration=0.2) #click it
        #     print('Practice Again Clicked')
        #     time.sleep(5) #wait for the page to load
        # start_loc = pyautogui.locateOnScreen('start_practice.png')
        # if str(start_loc) != 'None': #start practice is there
        #     start_loc = pyautogui.center(start_loc)
        #     pyautogui.click(start_loc, duration=0.2) #click it
        #     print('Start Practice Clicked')
        #    time.sleep(1)
        #Quiz Cases
        print('entering quiz cases')
        numcases = 18
        for i in range(0,numcases):

            job = braille(870, 280, 1300, 280, False)
            print(job)

            if job == 'Write this in English':
                germ = braille(850, 330, 1300, 330, True)
                pyautogui.click(1000, 400, duration=0.1)#return focus to textbox
                translist = germ.split(' ')
                for i in translist:
                    if str(i) == 'ich':
                        pyautogui.typewrite('I ')
                    elif str(i) == 'bin':
                        pyautogui.typewrite('am ')
                    elif str(i) == 'und':
                        pyautogui.typewrite('and ')
                    elif str(i) == 'du':
                        pyautogui.typewrite('you ')
                    elif str(i) == 'brot':
                        pyautogui.typewrite('bread ')
                    elif str(i) == 'wasser':
                        pyautogui.typewrite('water ')
                    elif str(i) == 'trinkt':
                        pyautogui.typewrite('drinks ')
                    elif str(i) == 'kind':
                        pyautogui.typewrite('child ')
                    elif str(i) == 'mann':
                        pyautogui.typewrite('man ')
                    elif str(i) == 'frau':
                        pyautogui.typewrite('woman ')
                    elif str(i) == 'mdchen':
                        pyautogui.typewrite('girl ')
                    elif str(i) == 'junge':
                        pyautogui.typewrite('boy ')
                    elif str(i) == 'er':
                        pyautogui.typewrite('he ')
                    elif str(i) == 'sie':
                        pyautogui.typewrite('she ')
                    elif str(i) == 'es':
                        pyautogui.typewrite('it ')
                    elif str(i) == 'ist':
                        pyautogui.typewrite('is ')
                    elif str(i) == 'bist':
                        pyautogui.typewrite('are ')
                    elif str(i) == 'eine' or str(i) == 'ein':
                        pyautogui.typewrite('a ')
                    else:
                        pyautogui.typewrite(i + ' ')
            elif job == 'Write this in German':
                engl = braille(850, 330, 1300, 330, True)
                pyautogui.click(1000, 400, duration=0.2)#return focus to textbox
                translist = engl.split(' ')
                for i in translist:
                    if str(i) == 'i' or str(i) == 'me':
                        pyautogui.typewrite('ich ')
                    elif str(i) == 'am':
                        pyautogui.typewrite('bin ')
                    elif str(i) == 'and':
                        pyautogui.typewrite('und ')
                    elif str(i) == 'you':
                        pyautogui.typewrite('du ')
                    elif str(i) == 'bread':
                        pyautogui.typewrite('Brot ')
                    elif str(i) == 'water':
                        pyautogui.typewrite('Wasser ')
                    elif str(i) == 'drinks':
                        pyautogui.typewrite('trinkt ')
                    elif str(i) == 'child':
                        pyautogui.typewrite('Kind ')
                    elif str(i) == 'man':
                        pyautogui.typewrite('Mann ')
                    elif str(i) == 'woman':
                        pyautogui.typewrite('Frau ')
                    elif str(i) == 'girl':
                        pyautogui.typewrite('Madchen ')#:'( ä ain't work
                    elif str(i) == 'boy':
                        pyautogui.typewrite('Junge ')
                    elif str(i) == 'he':
                        pyautogui.typewrite('er ')
                    elif str(i) == 'she':
                        pyautogui.typewrite('sie ')
                    elif str(i) == 'it':
                        pyautogui.typewrite('es ')
                    elif str(i) == 'is':
                        pyautogui.typewrite('ist ')
                    elif str(i) == 'are':
                        pyautogui.typewrite('bist ')
                    elif str(i) == 'a':
                        pyautogui.typewrite('ein ')
                    else:
                        pyautogui.typewrite(i + ' ')
            elif job == 'Select the missing word':
                dat = braille(860, 330, 1400, 600, False)
                #custom parsing
                dat = re.sub('[^A-Za-z 0-9\n]', '', dat)
                dat = dat.lower()
                translist = dat.split('\n')

                #defining a bunch of variables that are unncesary
                ein = ''
                eine = ''
                bin = ''
                ist = ''
                sein = ''
                bist = ''

                instr = translist[0]
                for i in range(1, len(translist)):
                    translist[i] = re.sub('[^A-Za-z]', '', translist[i])
                    if translist[i] == 'ein':
                        ein = i
                    elif translist[i] == 'eine':
                        eine = i
                    elif translist[i] == 'bin':
                        bin = i
                    elif translist[i] == 'ist':
                        ist = i
                    elif translist[i] == 'sein':
                        sein = i
                    elif translist[i] == 'bist':
                        bist = i
                if 'mann' in instr:
                    pyautogui.typewrite(str(ein))
                elif 'junge' in instr:
                    pyautogui.typewrite(str(ein))
                elif 'frau' in instr:
                    pyautogui.typewrite(str(eine))
                if 'du' in instr:
                    pyautogui.typewrite(str(bist))

                print("I hope this works...")
            elif job == 'Mark all correct meanings':
                dat = braille(860, 330, 1400, 600, False)
                #custom parsing
                dat = re.sub('[^A-Za-z \n]', '', dat)
                dat = dat.lower()
                translist = dat.split('\n')

                instr = translist[0]
                one = translist[1]
                one = one + ' '
                two = translist[2]
                two = two + ' '
                three = translist[3]
                three = three + ' '

                print(instr)
                print(one)
                print(two)
                print(three)

                to_trans = instr.split(' ')

                instr = ''

                for i in to_trans:
                    if str(i) == 'i' or str(i) == 'me':
                        instr = instr + 'ich '
                    elif str(i) == 'am':
                        instr = instr + 'bin '
                    elif str(i) == 'and':
                        instr = instr + 'und '
                    elif str(i) == 'you':
                        instr = instr + 'du '
                    elif str(i) == 'bread':
                        instr = instr + 'brot '
                    elif str(i) == 'water':
                        instr = instr + 'wasser '
                    elif str(i) == 'drinks':
                        instr = instr + 'trinkt '
                    elif str(i) == 'child':
                        instr = instr + 'kind '
                    elif str(i) == 'man':
                        instr = instr + 'mann '
                    elif str(i) == 'woman':
                        instr = instr + 'frau '
                    elif str(i) == 'girl':
                        instr = instr + 'mdchen '#:'( ä ain't work
                    elif str(i) == 'boy':
                        instr = instr + 'junge '
                    elif str(i) == 'he':
                        instr = instr + 'er '
                    elif str(i) == 'she':
                        instr = instr + 'sie '
                    elif str(i) == 'it':
                        instr = instr + 'es '
                    elif str(i) == 'is':
                        instr = instr + 'ist '
                    elif str(i) == 'are':
                        instr = instr + 'bist '
                    elif str(i) == 'a':
                        instr = instr + 'ein '
                    else:
                        instr = instr + i + ' '

                    print(instr)

                typed = 0
                if one == instr:
                    pyautogui.typewrite('1')
                    typed = 1
                elif two == instr:
                    pyautogui.typewrite('2')
                    typed = 1
                elif three == instr:
                    pyautogui.typewrite('3')
                    typed = 1
                if typed == 0:
                    instr = instr.replace('ein', 'eine')
                    print(instr)
                    if one == instr:
                        pyautogui.typewrite('1')
                    elif two == instr:
                        pyautogui.typewrite('2')
                    elif three == instr:
                        pyautogui.typewrite('3')

            elif job == 'Mark the correct meaning':
                dat = braille(860, 330, 1400, 600, False)
                #custom parsing

                dat = re.sub('[^A-Za-z \n]', '', dat)
                dat = dat.lower()
                translist = dat.split('\n')

                instr = translist[0]
                one = translist[1]
                one = one + ' '
                two = translist[2]
                two = two + ' '
                three = translist[3]
                three = three + ' '

                print(instr)
                print(one)
                print(two)
                print(three)

                to_trans = instr.split(' ')

                instr = ''

                for i in to_trans:
                    if str(i) == 'i' or str(i) == 'me':
                        instr = instr + 'ich '
                    elif str(i) == 'am':
                        instr = instr + 'bin '
                    elif str(i) == 'and':
                        instr = instr + 'und '
                    elif str(i) == 'you':
                        instr = instr + 'du '
                    elif str(i) == 'bread':
                        instr = instr + 'brot '
                    elif str(i) == 'water':
                        instr = instr + 'wasser '
                    elif str(i) == 'drinks':
                        instr = instr + 'trinkt '
                    elif str(i) == 'child':
                        instr = instr + 'kind '
                    elif str(i) == 'man':
                        instr = instr + 'mann '
                    elif str(i) == 'woman':
                        instr = instr + 'frau '
                    elif str(i) == 'girl':
                        instr = instr + 'mdchen '#:'( ä ain't work
                    elif str(i) == 'boy':
                        instr = instr + 'junge '
                    elif str(i) == 'he':
                        instr = instr + 'er '
                    elif str(i) == 'she':
                        instr = instr + 'sie '
                    elif str(i) == 'it':
                        instr = instr + 'es '
                    elif str(i) == 'is':
                        instr = instr + 'ist '
                    elif str(i) == 'are':
                        instr = instr + 'bist '
                    elif str(i) == 'a':
                        instr = instr + 'ein '
                    else:
                        instr = instr + i + ' '

                    print(instr)

                #this is getting to be such a mess
                instr = instr.replace('ist drinking', 'trinkt')
                if instr == 'ist sie drinking ':
                    instr = 'trinkt sie '
                elif instr == 'does er drink ':
                    instr = 'trinkt er '
                elif instr == 'du bist ein mdchen ':
                    instr = 'sie sind ein mdchen '
                elif instr == 'du bist ein frau und ich bin ein mann ':
                    instr = 'sie sind eine frau und ich bin ein mann '
                elif instr == 'ein frau ein mdchen ':
                    instr = 'eine frau ein mdchen '
                elif instr == 'du bist ein frau ':
                    instr = 'sie sind eine frau '
                elif instr == 'du bist ein mann ':
                    instr = 'sie sind ein mann '
                typed = 0
                if one == instr:
                    pyautogui.typewrite('1')
                    typed = 1
                elif two == instr:
                    pyautogui.typewrite('2')
                    typed = 1
                elif three == instr:
                    pyautogui.typewrite('3')
                    typed = 1
                if typed == 0:
                    instr = instr.replace('ein', 'eine')
                    print(instr)
                    if one == instr:
                        pyautogui.typewrite('1')
                    elif two == instr:
                        pyautogui.typewrite('2')
                    elif three == instr:
                        pyautogui.typewrite('3')

            elif job == 'Write “girl” in German':
                pyautogui.click(1300, 440, duration=0.2)
                pyautogui.typewrite('Madchen')
            elif job == 'Write “woman” in German':
                pyautogui.click(1300, 440, duration=0.2)
                pyautogui.typewrite('Frau')
            elif job == 'Write “boy” in German':
                pyautogui.click(1300, 440, duration=0.2)
                pyautogui.typewrite('Junge')
            elif job == 'Type what you hear':
                find_click('cannot_hear.png')
                time.sleep(.5)
                find_click('continue.png')
            else:
                break

            next()

except KeyboardInterrupt:
    print('\nTerminating.')
