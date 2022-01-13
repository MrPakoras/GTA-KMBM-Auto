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

def kbp(key,n): # key press
	for loop in range(n):
		pdi.press(key)
		print(key)
		time.sleep(0.1)

def pync(): # pynput click
	pyn_mouse.press(Button.left)
	time.sleep(0.1)
	pyn_mouse.release(Button.left)
	time.sleep(0.5)


# Prog
n = 0

def main():
	time.sleep(2)
	# pdi.moveTo(res[0]//2, res[1]//2) # centre mouse
	# Enter Bunker
	# Start in Teleport section of mod menu

	## TP to laptop
	kbp(down_key, 5)
	kbp(enter_key,1) # Custom locations

	## Use laptop
	kbp(down_key,1) # Change n to whichever location your bunker laptop is
	kbp(enter_key,1) # TP to laptop
	time.sleep(0.5)

	kbp('t',1) # Sit on chair
	time.sleep(7)
	kbp('enter',1) # Press Enter to open laptop

	time.sleep(1)

	## Resupply
	global n
	if n == 20:
		pdi.moveTo(round(res[0]*1/5),round(res[1]*0.45)) # resupply button
		pync()
		pdi.moveTo(round(res[0]*2/5),round(res[1]*5/7)) # Click steal button
		pync()
		pdi.moveTo(round(res[0]*0.55),round(res[1]*4/7)) # Click Confirm button
		pync()
		time.sleep(10)
		n = 0

	## Selling stock
	pdi.moveTo(res[0]//2, round(res[1]*0.6)) # Click Enter laptop button
	time.sleep(1)
	# pdi mouse clicks werent working in game so had to use pynput
	pync()

	pdi.moveTo(round(res[0]*1/5),round(res[1]*4/7)) # Click Sell Stock button
	pync()

	pdi.moveTo(round(res[0]*2/5),round(res[1]*5/7)) # Click Sell to LS button
	pync()

	pdi.moveTo(round(res[0]*0.55),round(res[1]*4/7)) # Click Confirm button
	pync()

	time.sleep(5)

	## Navigate to Bunker Settings in mod menu
	kbp(back_key,2)
	kbp(down_key,3)
	kbp(enter_key,2)
	kbp(down_key,1)

	## Increase payout to 2 mill
	for loop in range(200):
		pdi.keyDown(right_key)
	pdi.keyUp(right_key)

	kbp(enter_key,1)

	# ## Re-enter bunker
	# for loop in range(20):
	# 	pdi.keyDown('s')
	# 	kbp('d',1)
	# pdi.keyUp('s')


	## Restock supplies
	kbp(down_key,1)
	kbp(enter_key,1)

	## Navigate back to Teleport section
	kbp(back_key,2)
	kbp(up_key,3)
	kbp(enter_key,1)

	## TP to Bunker
	kbp(down_key, 5)
	kbp(enter_key,1)
	kbp(down_key, 2)
	kbp(enter_key,1) # Custom location bunker
	kbp(back_key,1)
	kbp(up_key,5) # Return to top


	time.sleep(5)

	n += 1 # loops
	

while True:
	main()
