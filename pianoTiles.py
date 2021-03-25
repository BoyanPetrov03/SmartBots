from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 P

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("q") == False:
    if (pyautogui.pixel(318, 650) [0] == 0):
        click(318, 650)
    if (pyautogui.pixel(426, 650) [0] == 0):
        click(426, 650)
    if (pyautogui.pixel(538, 650) [0] == 0):
        click(538, 650)
    if (pyautogui.pixel(624, 650) [0] == 0):
        click(624, 650)

print("dedov")
