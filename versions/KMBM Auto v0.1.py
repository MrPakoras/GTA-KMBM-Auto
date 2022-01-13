# Kiddions Mod Bunker Mission Automater

from pynput.keyboard import Key, Controller
import time

kb = Controller() # Keyboard

# Keys
up_key = 'i'
down_key = 'k'
left_key = 'j'
right_key = 'l'
back_key = 'u'
enter_key = 'o'

def kbp(key):
	kb.press(key)
	kb.release(key)
	print(key)
	time.sleep(0.5)

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
	time.sleep(2)

	kbp('t') # Sit on chair
	time.sleep(3)
	kbp(Key.enter) # Press Enter to open laptop

main()