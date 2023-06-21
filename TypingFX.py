import time, sys, os

length = 0.03

def clearScreen():
	os.system("clear") #clears whatever is on the screen

def tPrint(text): #delays the speed the text is revealed at.
	print()
	for char in text:
		sys.stdout.write(char)#referencing sites online.
		sys.stdout.flush()
		time.sleep(length)

def tInput(text): #this delays texts for the input command
	print()
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(length)
	value = input()
	return value

def tIntInput(text): #intinput
	print()
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(length)
	value = int(input())
	return value