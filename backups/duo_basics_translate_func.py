#!/usr/bin/env python
# duo_basics.py - completes German Basics 1 a specified number of times
#not very dynamic tbh

import pyautogui, time, re, random

#clipboard functionality
import tkinter as tk
root = tk.Tk()
root.withdraw()

keys = ['ich', 'bin', 'und', 'du', 'brot', 'wasser', 'trinkt', 'kind', 'mann', 'frau', 'mdchen', 'junge', 'er', 'sie', 'es', 'ist', 'bist', 'eine', 'ein']
values = ['i', 'am', 'and', 'you', 'bread', 'water', 'drinks', 'child', 'man', 'woman', 'girl', 'boy', 'he', 'she', 'it', 'is', 'are', 'a', 'a']
dcty = dict(zip(keys, values))
pairs = dcty.items()
print (pairs)

def next():
    check = pyautogui.locateOnScreen('check.png')
    if str(check) != 'None':
        check = pyautogui.center(check)
        pyautogui.click(check, duration=0.2)
    else:
        find_click('skip.png')
        find_click('wrong.png')
    wrong = pyautogui.locateOnScreen('wrong.png')
    if str(wrong) != 'None':
        wrong = pyautogui.center(wrong)
        pyautogui.click(wrong, duration=0.2)
    else:
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

def translate(str):
    strlist = str.split(' ')
    trans_str = ''
    for x in strlist:
        a = next((i for i, j in enumerate(pairs) if j[0] == ), None)
    if len(trans_str) < i+1:
        trans_str = trans_str + group[i]
    return trans_str

print('Welcome to your very own Duo doer.')
print('This program is not currently very dynamic.')
print('Please ensure that duolingo is in a chrome tab on the right half of the screen.')
print('Remember to not let anything obscure the duolingo window.')
rep = int(input('How many iterations would you like to perform?\n'))

try:
    while rep > 0:
        rep = rep - 1 #Loop for as many times as user specifies
        print('Use Ctrl+C with this window in focus to stop at any time.')
        #which button is there?
        again_loc = pyautogui.locateOnScreen('practice_again.png')
        if str(again_loc) != 'None': #practice again is present
            again_loc = pyautogui.center(again_loc)
            pyautogui.click(again_loc, duration=0.2) #click it
            print('Practice Again Clicked')
            time.sleep(2) #wait for the page to load
        start_loc = pyautogui.locateOnScreen('start_practice.png')
        if str(start_loc) != 'None': #start practice is there
            start_loc = pyautogui.center(start_loc)
            pyautogui.click(start_loc, duration=0.2) #click it
            print('Start Practice Clicked')
            time.sleep(1)
        #Quiz Cases
        print('entering quiz cases')
        while str(pyautogui.locateOnScreen('practice_again.png')) == 'None':

            job = braille(870, 280, 1300, 280, False)
            print(job)

            if job == 'Write this in English':
                germ = braille(850, 330, 1300, 330, True)
                pyautogui.click(1000, 400, duration=0.1)#return focus to textbox
                pyautogui.typewrite(translate(germ))
                # translist = germ.split(' ')
                # for i in translist:
                #     if str(i) == 'ich':
                #         pyautogui.typewrite('I ')
                #     elif str(i) == 'bin':
                #         pyautogui.typewrite('am ')
                #     elif str(i) == 'und':
                #         pyautogui.typewrite('and ')
                #     elif str(i) == 'du':
                #         pyautogui.typewrite('you ')
                #     elif str(i) == 'brot':
                #         pyautogui.typewrite('bread ')
                #     elif str(i) == 'wasser':
                #         pyautogui.typewrite('water ')
                #     elif str(i) == 'trinkt':
                #         pyautogui.typewrite('drinks ')
                #     elif str(i) == 'kind':
                #         pyautogui.typewrite('child ')
                #     elif str(i) == 'mann':
                #         pyautogui.typewrite('man ')
                #     elif str(i) == 'frau':
                #         pyautogui.typewrite('woman ')
                #     elif str(i) == 'mdchen':
                #         pyautogui.typewrite('girl ')
                #     elif str(i) == 'junge':
                #         pyautogui.typewrite('boy ')
                #     elif str(i) == 'er':
                #         pyautogui.typewrite('he ')
                #     elif str(i) == 'sie':
                #         pyautogui.typewrite('she ')
                #     elif str(i) == 'es':
                #         pyautogui.typewrite('it ')
                #     elif str(i) == 'ist':
                #         pyautogui.typewrite('is ')
                #     elif str(i) == 'bist':
                #         pyautogui.typewrite('are ')
                #     elif str(i) == 'eine' or str(i) == 'ein':
                #         pyautogui.typewrite('a ')
                #     else:
                #         pyautogui.typewrite(i + ' ')
            elif job == 'Write this in German':
                engl = braille(850, 330, 1300, 330, True)
                pyautogui.click(1000, 400, duration=0.2)#return focus to textbox
                # translist = engl.split(' ')
                # for i in translist:
                #     if str(i) == 'i' or str(i) == 'me':
                #         pyautogui.typewrite('ich ')
                #     elif str(i) == 'am':
                #         pyautogui.typewrite('bin ')
                #     elif str(i) == 'and':
                #         pyautogui.typewrite('und ')
                #     elif str(i) == 'you':
                #         pyautogui.typewrite('du ')
                #     elif str(i) == 'bread':
                #         pyautogui.typewrite('Brot ')
                #     elif str(i) == 'water':
                #         pyautogui.typewrite('Wasser ')
                #     elif str(i) == 'drinks':
                #         pyautogui.typewrite('trinkt ')
                #     elif str(i) == 'child':
                #         pyautogui.typewrite('Kind ')
                #     elif str(i) == 'man':
                #         pyautogui.typewrite('Mann ')
                #     elif str(i) == 'woman':
                #         pyautogui.typewrite('Frau ')
                #     elif str(i) == 'girl':
                #         pyautogui.typewrite('Madchen ')#:'( ä ain't work
                #     elif str(i) == 'boy':
                #         pyautogui.typewrite('Junge ')
                #     elif str(i) == 'he':
                #         pyautogui.typewrite('er ')
                #     elif str(i) == 'she':
                #         pyautogui.typewrite('sie ')
                #     elif str(i) == 'it':
                #         pyautogui.typewrite('es ')
                #     elif str(i) == 'is':
                #         pyautogui.typewrite('ist ')
                #     elif str(i) == 'are':
                #         pyautogui.typewrite('bist ')
                #     elif str(i) == 'a':
                #         pyautogui.typewrite('ein ')
                #     else:
                #         pyautogui.typewrite(i + ' ')
            elif job == 'Select the missing word':

                #x2 = 1500 y2 = 600
                #x1 = 875 y1 330

                pyautogui.typewrite('1')
                time.sleep(.2)
                pyautogui.typewrite(str(random.randint(1, 4)))
                print("I don't know how to do that yet...")
            elif job == 'Mark all correct meanings':
                dat = braille(860, 330, 1200, 600, False)
                #custom parsing
                phrase.replace('?', '.')
                phrase = re.sub('[^A-Za-z .]', '', phrase)
                phrase = phrase.lower()
                translist = dat.split('.')

                inst = translist[0]
                one = translist[1]
                two = translist[2]
                three = translist[3]

                to_trans = inst.split(' ')

                for i in to_trans:


                pyautogui.typewrite(str(random.randint(1, 3)))
                print("I don't know how to do that yet...")
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
