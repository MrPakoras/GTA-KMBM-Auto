import pyautogui, time, ctypes, math, pywinauto, mouse, time
import pydirectinput as pdi
from pynput.mouse import Button, Controller

user32 = ctypes.windll.user32
res = user32.GetSystemMetrics(0),user32.GetSystemMetrics(1) # screen resolution
print(res)

time.sleep(2)
pyn_mouse = Controller()

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

# pdi.moveTo(round(res[0]*1/5),round(res[1]*0.45)) # resupply button

# pdi.moveTo(round(res[0]*2/5),round(res[1]*5/7)) # sell to LS

# pdi.moveTo(round(res[0]*0.55),round(res[1]*4/7)) # confirm

# pdi.keyDown('a')
# time.sleep(2)
# pdi.keyUp('a')

# for loop in range(20):
# 	pdi.keyDown('a')

# for loop in range(30):
# 	pdi.keyDown('s')
# pdi.keyUp('s')
# mx,my = round(res[0]*0.5),round(res[1]*0.1)
# print(mx,my)

# pdi.moveTo(mx,my) 

# for loop in range(30):
# 	pdi.keyDown('s')
# pdi.keyUp('s')

# def pync(): # pynput click
# 	pyn_mouse.press(Button.left)
# 	time.sleep(0.1)
# 	pyn_mouse.release(Button.left)
# 	time.sleep(0.5)


# pdi.moveTo(round(res[0]*1/5),round(res[1]*0.45)) # resupply button
# pync()
# pdi.moveTo(round(res[0]*2/5),round(res[1]*5/7)) # Click steal button
# pync()
# pdi.moveTo(round(res[0]*0.55),round(res[1]*4/7)) # Click Confirm button
# pync()


with open('../log.txt','a+') as file:
	print('starting...')
	start = time.time()
	# time.sleep(10)
	total = time.time()-start
	dt = time.strftime('%d/%m/%y %I:%M:%S%p')
	print(f'>> {dt} - Sequence took {total} seconds.')

	file.seek(0)
	file.write(f'>> {dt} - Sequence took {total} seconds.\n')
	file.close()
	
