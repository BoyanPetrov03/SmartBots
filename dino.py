from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while keyboard.is_pressed('q') == False:
    if (pyautogui.pixel(274, 414))[0] == 83:
        keyboard.press('space')
