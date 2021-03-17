#!/usr/bin/env python
# duo_basics.py - completes German Basics 1 a specified number of times

import pyautogui, time
import tkinter as tk #clipboard functionality

def next():
    check = pyautogui.locateOnScreen('check.png')
    if str(check) != 'None':
        check = pyautogui.center(check)
        pyautogui.click(check, duration=0.2)
        time.sleep(.2)
    else:
        find_click('skip.png')
        find_click('wrong.png')
    wrong = pyautogui.locateOnScreen('wrong.png')
    if str(wrong) != 'None':
        wrong = pyautogui.center(wrong)
        pyautogui.click(wrong, duration=0.2)
    else:
        time.sleep(.2)
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

print('Welcome to your very own Duo doer.')
rep = int(input('How many iterations would you like to perform?\n'))


try:
    while rep > 0:
        rep = rep - 1 #Loop for as many times as user specifies
        print('Use Ctrl+C to stop at any time.')
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
            write_eng = pyautogui.locateOnScreen('write_eng.png')
            print('write eng = ' + str(write_eng))
            if str(write_eng) != 'None':
                #make sure text box is in focus
                temp = pyautogui.center(write_eng)
                pyautogui.moveTo(temp, duration=0.2)
                pyautogui.moveRel(0,200, duration=0.2)
                pyautogui.click()
                #all cases need to be covered here
                pyautogui.typewrite('Bread water')
                #
                next()
            else: #eng not found -> look for deu
                write_deu = pyautogui.locateOnScreen('write_deu.png')
                print('write deu = ' + str(write_deu))
                if str(write_deu) != 'None':
                    #write in german cases
                    pyautogui.typewrite('Frau')
                    next()
                else: #deu not found -> look for missing
                    slct_missing = pyautogui.locateOnScreen('missing_word.png')
                    print('Select missing = ' + str(slct_missing))
                    if str(slct_missing) != 'None':
                        #all selection cases
                        _frau = pyautogui.locateOnScreen('_frau.png')
                        if str(_frau) != 'None':
                            find_click('cap_eine.png')
                        else:
                            bin_frau = pyautogui.locateOnScreen('bin_frau.png')
                            if str(bin_frau) != 'None':
                                if find_click('eine1.png') == -1:#the image was not found
                                    find_click('eine2.png')
                            else:
                                _mann = pyautogui.locateOnScreen('_mann.png')
                                if str(_mann) != 'None':
                                    find_click('ein.png')
                                else:
                                    du_ = pyautogui.locateOnScreen('du_.png')
                                    if str(du_) != 'None':
                                        find_click('bist3.png')
                        next()
                    else: #missing not found, look for mark all
                        mark_all = pyautogui.locateOnScreen('mark_correct.png')
                        print('mark all = ' + str(mark_all))
                        if str(mark_all) != 'None':
                            #mark all cases
                            next()
                        else: # mark all not found, look for listen
                            type_hear = pyautogui.locateOnScreen('listen.png')
                            print('listen checked')
                            if str(type_hear) != 'None':
                                find_click('cannot_hear.png')
                                time.sleep(1)
                                find_click('continue.png')


except KeyboardInterrupt:
    print('\nTerminating.')



#x, y = pyautogui.position()
#disp_pos = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#print(disp_pos)

#NOTES
#
#Enter can be used for continuing
#You can find an exact image anywhere on the screen and click it
#
#
#
#
#
#DUOLINGO BASICS ELEMENTS
#Write this in English - Type in box
#   Ein Kind und ein Mann - A child and a man
#   Brot, Wasser - Bread water
#   Ich und du - I and you
#   brot und wasser - bread and water
#   du und ich
#   er sie es
#
#
#Mark all correct meanings - long buttons for clicking
#   does he drink - trinkt er
#   He is a man - er ist ein Mann
#    a girl is a child
#
#Write this in German - Type in box
#   me and you - ich und du
#   you and me - du und ich
#   he she it
#   woman
#
#
#Select the missing word - Short button clicking
#   ______ Frau - Eine
#   Ich ____ eine Frau - bin
#
#
#Type what you hear
#   ... click Can't listen now
#
#
#Click on Practice again after that
#
#
#
#
#
#
#
#
#
