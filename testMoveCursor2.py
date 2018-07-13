import sys
import time
import pyautogui
import math

cursor_pos_description = ["up", "left", "down", "right"]
screen_w, screen_h = pyautogui.size();

for i in range(360) :
    m = i % 4
    print(pyautogui.position())
    #360 degree
    pyautogui.moveTo((screen_w / 2 - 15) * math.cos(i*3.14/180) + screen_w / 2, (screen_h / 2 - 10) * math.sin(i*3.14/180) + screen_h / 2) 
    
    time.sleep(0.1)

'''
for i in range(10) :
    print(pyautogui.position())
    time.sleep(1)
'''
