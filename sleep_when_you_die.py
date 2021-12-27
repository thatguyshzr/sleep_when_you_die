import pyautogui
import win32api

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

mins= 5

while(True):
	idle= int((win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0)
	print(idle)
	if idle!=0 and idle%(mins*60) == 0:    # if idle for 5 mins
		pyautogui.press('capslock')
		pyautogui.press('capslock')

