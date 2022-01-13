import pyautogui, time, ctypes, math, pywinauto, mouse
import pydirectinput as pdi
from pynput.mouse import Button, Controller

user32 = ctypes.windll.user32
res = user32.GetSystemMetrics(0),user32.GetSystemMetrics(1) # screen resolution


time.sleep(2)

# print('pdi')
# pdi.click()
# time.sleep(2)

# print('pywinauto')
# pywinauto.mouse.click(button='left', coords=(500,500))
# time.sleep(2)

# print('pyautogui')
# pyautogui.click()
# time.sleep(2)

# print('mouse')
# mouse.click('left')
# time.sleep(2)

# print('pynput')
# mouse = Controller()
# mouse.click(Button.left, 1)
# time.sleep(2)

## WORKS
# print('pynput')
# mouse = Controller()
# mouse.press(Button.left)
# time.sleep(1)
# mouse.release(Button.left)
# time.sleep(2)

# pdi.moveTo(round(res[0]*1/5),round(res[1]*4/7)) # sell stock button

# pdi.moveTo(round(res[0]*2/5),round(res[1]*5/7)) # sell to LS

# pdi.moveTo(round(res[0]*0.55),round(res[1]*4/7)) # confirm

# pdi.keyDown('a')
# time.sleep(2)
# pdi.keyUp('a')

# for loop in range(20):
# 	pdi.keyDown('a')

for loop in range(30):
	pdi.keyDown('s')
pdi.keyUp('s')
