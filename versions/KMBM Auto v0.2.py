# Kiddions Mod Bunker Mission Automater

import pyautogui, time, ctypes, math, pywinauto
import pydirectinput as pdi
from pynput.mouse import Button, Controller

user32 = ctypes.windll.user32
res = user32.GetSystemMetrics(0),user32.GetSystemMetrics(1) # screen resolution

pyn_mouse = Controller() # pynput mouse

# Keys
up_key = 'i'
down_key = 'k'
left_key = 'j'
right_key = 'l'
back_key = 'u'
enter_key = 'o'

# def kbp(key):
# 	kb.press(key)
# 	kb.release(key)
# 	print(key)
# 	time.sleep(0.5)

def kbp(key): # key press
	pdi.press(key)
	print(key)
	time.sleep(0.1)

def pync(): # pynput click
	pyn_mouse.press(Button.left)
	time.sleep(0.1)
	pyn_mouse.release(Button.left)
	time.sleep(2)


# Prog

def main():
	time.sleep(2)
	# Enter Bunker
	# Start in Teleport section of mod menu
	for loop in range(5):
		kbp(down_key)
		# time.sleep(1)
	kbp(enter_key) # Custom locations

	for loop in range(1): # Change this to whichever location your bunker laptop is
		kbp(down_key)

	kbp(enter_key) # TP to laptop
	time.sleep(0.5)

	kbp('t') # Sit on chair
	time.sleep(5)
	kbp('enter') # Press Enter to open laptop

	time.sleep(1)

	pdi.moveTo(res[0]//2, round(res[1]*0.6)) # Click Enter laptop button
	time.sleep(1)
	# pdi mouse clicks werent working in game so had to use pynput
	pync()

	pdi.moveTo(round(res[0]*2/5),round(res[1]*5/7)) # Click Sell to LS button
	pync()

	pdi.moveTo(round(res[0]*0.55),round(res[1]*4/7)) # Click Confirm button
	pync()

	


main()
