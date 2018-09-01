#!/usr/local/bin/python
# coding: utf-8
import os, sys
import subprocess
import random
import time
import locale
import datetime

# Recommended terminal settings: Size: 38*38, Font: Speccy Medium 24p, Forground: White, Background: Black

# Settings:
margin1 = (" ") 		# Narrow left margin.
margin2 = ("  ") 		# Wide left margin.
columns = 12 			# Number of cards in a row
baseDifficulty = 0.5	# Time in seconds, higher is easier. (baseDifficulty / difficulty) * 34 gives total counting time.
# Game time at different baseDifficulty:
# baseDifficulty 0.3: [difficulty 1: 10.20sec.]  [difficulty 5: 2.04sec.]  [difficulty 9: 1.13sec.]
# baseDifficulty 0.5: [difficulty 1: 17.00sec.]  [difficulty 5: 3.40sec.]  [difficulty 9: 1.89sec.]
# baseDifficulty 1.0: [difficulty 1: 34.00sec.]  [difficulty 5: 6.80sec.]  [difficulty 9: 3.78sec.]
# baseDifficulty 2.0: [difficulty 1: 68.00sec.]  [difficulty 5: 13.60sec.] [difficulty 9: 7.56sec.]

# Various variables:
quantOfTheColor = (random.randrange(1, 58)) # The quantity of cards to count ranges from 1-58.
theCount = 0
colors = ["HEART", "SPADE", "DIAMOND", "CLUB"]
theColor = random.choice(colors)
difficulty = 0 # Selected in-game. To alter in code, change "baseDifficulty above"
tableSpace = ["freeSlot"] * 108 # This is a list for storing all the cards that will be placed on the "table"
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()


def placeTheColor(color):
# This function randomly places the cards to count in the tableSpace list.
	theColorLeft = quantOfTheColor
	while(theColorLeft > 0):
		trySlot = random.randrange(0, 107)
		if (tableSpace[trySlot] == "freeSlot"):
			tableSpace[trySlot] = theColor
			theColorLeft -= 1


def placeTheRest():
# This function iterates through the tableSpace list and places a random card (theColor excepted) when it finds a free slot.
	restOfColors = []
	for color in colors:
		if color != theColor:
			restOfColors.append(color)
	wordNum = 0
	for word in tableSpace:
		if word == "freeSlot":
			tableSpace[wordNum] = random.choice(restOfColors)
		wordNum += 1


def startScreen():
	global difficulty
	os.system('clear')
	print("\n\n")
	print(margin1 + "MISSION:\n" + margin1 + "COUNT ALL THE " + theColor + "S!")
	try:
		print("\n" + margin1 + "CHOOSE DIFFICULTY, 1-9\n" + margin1 + "(HIGHER IS HARDER)\n\n" + margin1 + "THEN PRESS ENTER TO BEGIN!")
		difficulty = int(input("\n\n\n\n\n\n\n >"))
	except ValueError:
	    print("\n\n" + "INTEGERS 1 THROUGH 9, WAS IT SO HARD?\n\n")
	    sys.exit(1)
	if ((difficulty < 1) or (difficulty > 9)):
	    print("\n\n" + "INTEGERS 1 THROUGH 9, WAS IT SO HARD?\n\n")
	    sys.exit(1)


def dealTheCards(width):
# This function iterates through the tableSpace list and prints the correct unicodes to the screen.
	os.system('clear')
	cardNumber = -1 # Have to offset this value to get even rows of cards
	for card in tableSpace:
		cardNumber += 1
		if cardNumber % width == 0: # When N number of cards have been printed, start a new line
			print("\n")
			print(margin2, end="")
# Below are a few escape sequences to change colors and to show unicode characters:
# "\33" is the escape character.
# "[31m" and "[30m" makes the text red or black respectively. "[107m" makes the background white.
# "[0m" resets
# u'\u2665' is the unicode for "Black Heart Suit"
# u'\u2660' is the unicode for "Black Spade Suit"
# u'\u2666' is the unicode for "Black Diamond Suit"
# u'\u2666' is the unicode for "Black Club Suit "
		if(card == "HEART"):
			print('\33[31m\33[107m' + (u"\u2665"), end="")
			print('\33[0m', end="  ")
		if(card == "SPADE"):
			print('\33[30m\33[107m' + (u'\u2660'), end="")
			print('\33[0m', end="  ")
		if(card == "DIAMOND"):
			print('\33[31m\33[107m' + (u'\u2666'), end="")
			print('\33[0m', end="  ")
		if(card == "CLUB"):
			print('\33[30m\33[107m' + (u'\u2663'), end="")
			print('\33[0m', end="  ")
	print('\33[0m', end="")
	print("\n")


def theStress():
# This function prints the moving bar showing the time left.
	sleepTime = (baseDifficulty / difficulty)
	print(margin2, end="")
	print('\33[32m\33[42m' + (u"\u2591"), end="\33[0m")
	time.sleep(sleepTime)
	print('\33[32m\33[42m' + (u"\u2591"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[32m\33[42m' + (u"\u2591"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[32m\33[42m' + (u"\u2591"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[33m\33[42m' + (u"\u2591"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[33m\33[42m' + (u"\u2591"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[33m\33[42m' + (u"\u2591"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[33m\33[42m' + (u"\u2591"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[33m\33[42m' + (u"\u2592"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[33m\33[42m' + (u"\u2592"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[33m\33[42m' + (u"\u2592"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[33m\33[42m' + (u"\u2592"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[33m\33[42m' + (u"\u2593"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[33m\33[42m' + (u"\u2593"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[33m\33[42m' + (u"\u2593"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[33m\33[43m' + (u"\u2593"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[33m\33[43m' + (u"\u2593"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[33m\33[43m' + (u"\u2593"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[33m\33[43m' + (u"\u2593"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[31m\33[43m' + (u"\u2591"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[31m\33[43m' + (u"\u2591"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[31m\33[43m' + (u"\u2591"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[31m\33[43m' + (u"\u2592"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[31m\33[43m' + (u"\u2592"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[31m\33[43m' + (u"\u2592"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[31m\33[43m' + (u"\u2592"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[31m\33[43m' + (u"\u2593"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[31m\33[43m' + (u"\u2593"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[31m\33[43m' + (u"\u2593"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[31m\33[43m' + (u"\u2593"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[31m\33[41m' + (u"\u2593"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[31m\33[41m' + (u"\u2593"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[31m\33[41m' + (u"\u2593"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print('\33[31m\33[41m' + (u"\u2593"), end="\33[0m")
	sys.stdout.flush()
	time.sleep(sleepTime)
	print("\n\n" + margin1 + "IS IT FUN BEING A SMARTASS??") # In case someone cheats by scrolling up
	for i in range(14):
		print("\n")

def theAnswer():
	global theCount
	try:
		print("\n" + margin1 + "ALRIGHT,\n\n" + margin1 + "HOW MANY " + theColor + "S DID YOU SEE?")
		theCount = int(input("\n\n\n\n\n\n >"))
	except ValueError:
	    print(margin1 + "I ASKED FOR A NUMBER, YOU IMBECILE!\n\n")
	    sys.exit(1)

def theScore():
	global endScore
# The score is calculated as follows:
	percentRight = (((quantOfTheColor - abs(quantOfTheColor-theCount)) / quantOfTheColor) * 100)
	if percentRight < 70:
		ratioScore = (percentRight * 0.1)
	if  percentRight >= 70:
		ratioScore = (percentRight * 1.0)
	if  percentRight >= 80:
		ratioScore = (percentRight * 5.0)
	if  percentRight >= 90:
		ratioScore = (percentRight * 10.0)
	if  percentRight == 100:
		ratioScore = (percentRight * 30.0)
	if quantOfTheColor < 10:
		newQuant = 10 # The ratioScore is the minumum endScore
	else:
		newQuant = quantOfTheColor
	endScore = int((ratioScore * difficulty) * (newQuant / 10)) # The game keeps the change


def checkHighscore(endScore):
	filename = (os.path.dirname(__file__) + '/CChigh.txt')
	try:
		HSfile = open(filename,'r')
		highScore = HSfile.readlines()
		HSfile.close()
	except:
		newHighscore()
	highColor = ""
	try:
		if (endScore > int(highScore[0])):
			newHighscore()
		else:
			if (len(highScore) == 7):
				if (highScore[4].rstrip() == "HEART"): highColor = (u"\u2665")
				if (highScore[4].rstrip() == "SPADE"): highColor = (u"\u2660")
				if (highScore[4].rstrip() == "DIAMOND"): highColor = (u"\u2666")
				if (highScore[4].rstrip() == "CLUB"): highColor = (u"\u2663")
				print("\n" + margin1 + "HIGHSCORE:  " + highScore[0].rstrip())
				print(margin1 + highScore[1].rstrip(), highScore[2].rstrip() + "/" + highScore[3].rstrip() + highColor, "DIFF:" + highScore[5].rstrip(), highScore[6].rstrip(), end="\n\n")
			else:
				newHighscore()
	except:
		sys.exit(1)


def newHighscore():
	print(" NEW HIGHSCORE!!!")
	sys.stdout.flush()
	time.sleep(3)
	os.system('clear')
	highName = input(" CONGRATULATIONS,\n YOU MADE THE ALL-TIME HIGHSCORE!\n\n PLEASE TYPE YOUR NAME (MAX 12 CHARS)\n\n\n\n >")
	highName = highName.upper()
	datum = []
	today = datetime.date.today()
	datum.append(today)
	filename = (os.path.dirname(__file__) + '/CChigh.txt')
	HSfile = open(filename,'w')
	HSfile.write(str(endScore) + "\n" + highName + "\n" + str(theCount) + "\n" + str(quantOfTheColor) + "\n" + theColor + "S\n" + str(difficulty) + "\n" + str(datum[0]))
	HSfile.close()



def endScreen(width):
# This function iterates slowly through the tableSpace list to print only the relevant cards, then prints the score.
	os.system('clear')
	print("\n\n")
	print(margin1 + "NOW, LET'S SEE HOW YOU DID!")
	time.sleep(1) 	  # A dramatic pause
	cardNumber = -1   # Have to offset this value to get even rows of cards
	theColorCount = 0 # For labeling the cards
	for card in tableSpace:
		cardNumber += 1
		if(cardNumber % width == 0):
			print("\n")
			print(margin2, end="")
		if(card == theColor):
			theColorCount += 1
			if(card == "HEART"):
				print('\33[31m\33[107m' + (u"\u2665"), end="")
				print('\33[0m\033[33m' + str(theColorCount).zfill(2), end="\33[0m")
			if(card == "SPADE"):
				print('\33[30m\33[107m' + (u'\u2660'), end="")
				print('\33[0m\033[33m' + str(theColorCount).zfill(2), end="\33[0m")
			if(card == "DIAMOND"):
				print('\33[31m\33[107m' + (u'\u2666'), end="")
				print('\33[0m\033[33m' + str(theColorCount).zfill(2), end="\33[0m")
			if(card == "CLUB"):
				print('\33[30m\33[107m' + (u'\u2663'), end="")
				print('\33[0m\033[33m' + str(theColorCount).zfill(2), end="\33[0m")
		else:
			print("   ", end="")
		sys.stdout.flush() # This is to force the print(). Without it, nothing is displayed until the loop is done.
		time.sleep(0.05) # Amount of time before the next card is shown
	print('\33[0m', end="") # Reset the escape sequences used for coloring the cards
	if (theCount == quantOfTheColor): # <------------------------------------------------------------------------ Ändra till quantOfTheColor
		print("\n\n\n" + margin1 + "\033[32;5mYOU COUNTED", str(theCount), theColor + "S.\n\n" + margin1 + "THE CORRECT ANSWER IS", str(quantOfTheColor) + "!\n\n\n" + margin1 + "YOUR SCORE: " + str(endScore) + "\33[0m\n\n\n\n\n")
	else:
		print("\n\n\n" + margin1 + "YOU COUNTED", str(theCount), theColor + "S.\n\n" + margin1 + "THE CORRECT ANSWER IS", str(quantOfTheColor) + "!\n\n\n" + margin1 + "YOUR SCORE: " + str(endScore))
	checkHighscore(endScore)

placeTheColor(theColor)
placeTheRest()
startScreen()
dealTheCards(columns)
theStress()
theAnswer()
theScore()
endScreen(columns)
