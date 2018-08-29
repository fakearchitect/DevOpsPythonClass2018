#!/usr/local/bin/python
# coding: utf-8
import os, sys
import random
#from random import randrange


# Gissa talet!
os.system('clear')
print("\n\n                         GUESS THE NUMBER!")
print("\n")
points = 100
randNum = random.randrange(0,100)
try:
    yourGuess = int(input("        Type an integer between 0 and 100, then press Enter.\n\n                                "))
except ValueError:
    print("\nHey, that's not an integer!")
    sys.exit(1)
if ((yourGuess < 0) or (yourGuess > 100)):
    print("\nI was very specific about the allowed range. Please don't try again.")
    sys.exit(1)
x = yourGuess
print("\n")

print("These are all the numbers between your guess and the correct number:\n")
if (randNum < x):
    #print(randNum)
    while(randNum != x):
        x = x - 1
        points = points - 1
        if (x != randNum):
            print(x, end=" ")
    print("\n")
elif (randNum == yourGuess):
    print("You guessed it right, you maniac!")
else:
    while(randNum != x):
        x = x + 1
        points = points - 1
        if (x != randNum):
            print(x, end=" ")
    print("\n")

print("-------------------------------------------------------------------\n")
print("\n")
print("                           Your guess:", yourGuess, "\n")
print("                        The right number:", randNum, "\n")
#print("\n")
print("               ", end="")

print("\n")
print("                >>>>>    Score:", points, "points!    <<<<<\n\n")
if (points == 100):
    print("                 Man, this stuff could make you rich!")
elif (points >= 80):
    print("                      Huh! That's pretty good!")
else:
    print("                    Better luck next time, pal!")
print("\n")
