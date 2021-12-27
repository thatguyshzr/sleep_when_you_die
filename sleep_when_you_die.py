import pyautogui
from random import randint
import win32api

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

current_pos_x, current_pos_y= pyautogui.position()
size_x, size_y= pyautogui.size()

while(True):
	idle= int((win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0)
	print(idle)
	if idle!=0 and idle%300 == 0:    # if idle for 5 mins
		pyautogui.press('capslock')
		pyautogui.press('capslock')

