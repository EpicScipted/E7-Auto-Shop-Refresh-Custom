# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:19:03 2020

@author: Usuario
"""


from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)
#Scroll at semi random place
#Aprox place X: 1263 Y:  590

while keyboard.is_pressed('q') == False:
    
    RB_pos=pyautogui.locateOnScreen('refresh_button.png')
#The confidence is added due to little variations in the background
    Coven_pos=pyautogui.locateOnScreen('covenant.png',confidence=0.95)
    Mystic_pos=pyautogui.locateOnScreen('mystic.png',confidence=0.95)
    time.sleep(0.5)
#Checks for covenant
    if (Coven_pos) != None:
        time.sleep(0.5)
        print("Buy Covenant Summons.")
        Coven_point=pyautogui.center(Coven_pos)
        #print("La pos en x seria...",Coven_point[0],"\nLa pos en y seria...", Coven_point[1])
        #Respecto de la pos original +800 en x y mas 50 en y es aprox donde esta el boton cuando el juego esta full screen
        click(Coven_point[0]+800, Coven_point[1]+50)
        click(Coven_point[0]+800, Coven_point[1]+50)
        time.sleep(0.5)#wait for confirm button
        Buy_button_Covenant_pos=pyautogui.locateOnScreen('Buy_button_Covenant.png')
        Buy_button_Covenant_point=pyautogui.center(Buy_button_Covenant_pos)
        click(Buy_button_Covenant_point[0], Buy_button_Covenant_point[1])
        click(Buy_button_Covenant_point[0], Buy_button_Covenant_point[1])
        time.sleep(0.5)
    else:
        print("No Covenant summons to buy.")       

#checks for mystic
    if (Mystic_pos) != None:
        time.sleep(0.5)        
        print("Buy Mystic Summons.")
        Mystic_point=pyautogui.center(Mystic_pos)
        #print("La pos en x seria...",Mystic_point[0],"\nLa pos en y seria...", Mystic_point[1])
        #Respecto de la pos original +800 en x y mas 50 en y es aprox donde esta el boton cuando el juego esta full screen
        click(Mystic_point[0]+800, Mystic_point[1]+50)
        click(Mystic_point[0]+800, Mystic_point[1]+50)
        time.sleep(0.5)#wait for confirm button
        Buy_button_Mystic_pos=pyautogui.locateOnScreen('Buy_button_Mystic.png')
        Buy_button_Mystic_point=pyautogui.center(Buy_button_Mystic_pos)
        click(Buy_button_Mystic_point[0], Buy_button_Mystic_point[1])
        click(Buy_button_Mystic_point[0], Buy_button_Mystic_point[1])
        time.sleep(0.5)
    else:
        time.sleep(0.5)
        print("No Mystic summons to buy.")
        click(x=1263,y=590)

    pyautogui.scroll(-5, x=1263, y=590)
    time.sleep(3)
    click(x=1263,y=590)
    Coven_pos2=pyautogui.locateOnScreen('covenant.png',confidence=0.95)
    Mystic_pos2=pyautogui.locateOnScreen('mystic.png',confidence=0.95)
	
#Checks for covenant
    if (Coven_pos2) != None:
        time.sleep(0.5)
        print("Buy Covenant Summons.")
        Coven_point=pyautogui.center(Coven_pos2)
        #print("La pos en x seria...",Coven_point[0],"\nLa pos en y seria...", Coven_point[1])
        #Respecto de la pos original +800 en x y mas 50 en y es aprox donde esta el boton cuando el juego esta full screen
        click(Coven_point[0]+800, Coven_point[1]+50)
        click(Coven_point[0]+800, Coven_point[1]+50)
        time.sleep(0.5)#wait for confirm button
        Buy_button_Covenant_pos=pyautogui.locateOnScreen('Buy_button_Covenant.png')
        Buy_button_Covenant_point=pyautogui.center(Buy_button_Covenant_pos)
        click(Buy_button_Covenant_point[0], Buy_button_Covenant_point[1])
        click(Buy_button_Covenant_point[0], Buy_button_Covenant_point[1])
        time.sleep(0.5)
    else:
        print("No Covenant summons to buy.")
        
#checks for mystic
    if (Mystic_pos2) != None:
        time.sleep(0.5)        
        print("Buy Mystic Summons.")
        Mystic_point=pyautogui.center(Mystic_pos2)
        #print("La pos en x seria...",Mystic_point[0],"\nLa pos en y seria...", Mystic_point[1])
        #Respecto de la pos original +800 en x y mas 50 en y es aprox donde esta el boton cuando el juego esta full screen
        click(Mystic_point[0]+800, Mystic_point[1]+50)
        click(Mystic_point[0]+800, Mystic_point[1]+50)
        time.sleep(0.5)#wait for confirm button
        Buy_button_Mystic_pos=pyautogui.locateOnScreen('Buy_button_Mystic.png')
        Buy_button_Mystic_point=pyautogui.center(Buy_button_Mystic_pos)
        click(Buy_button_Mystic_point[0], Buy_button_Mystic_point[1])
        click(Buy_button_Mystic_point[0], Buy_button_Mystic_point[1])
        time.sleep(0.5)
    else:
        print("No Mystic summons to buy.")
        click(x=1263,y=590)
        
#Finally refreshes
    RB_point=pyautogui.center(RB_pos)
    click(RB_point[0], RB_point[1])
    click(RB_point[0], RB_point[1])
    time.sleep(0.5)#wait for confirm to appear
    Confirm_pos=pyautogui.locateOnScreen('confirm button.png')
    Confirm_point=pyautogui.center(Confirm_pos)
    click(Confirm_point[0], Confirm_point[1])
    click(Confirm_point[0], Confirm_point[1])
    time.sleep(0.5)
        