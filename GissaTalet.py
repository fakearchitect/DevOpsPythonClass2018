#!/usr/local/bin/python
# coding: utf-8
import os, sys
import random
#from random import randrange


# Gissa talet!
os.system('clear')
print("\n\n                           GISSA TALET!")
print("\n")
points = 100
slump = random.randrange(0,100)
try:
    gissning = int(input("          Skriv ett tal mellan 0 och 100, och tryck retur.\n\n                                "))
except ValueError:
    print("\n           Du skrev inte ett giltigt tal!")
    sys.exit(1)
x = gissning
print("\n")

print("----Här är alla nummer mellan din gissning och det rätta svaret----\n")
if (slump < x):
    #print(slump)
    while(slump != x):
        x = x - 1
        points = points - 1
        if (x != slump):
            print(x, end=" ")
    print("\n")
elif (slump == gissning):
    print("Grattis du gissade rätt!")
else:
    while(slump != x):
        x = x + 1
        points = points - 1
        if (x != slump):
            print(x, end=" ")
    print("\n")

print("-------------------------------------------------------------------\n")
print("\n")
print("                         Din gissning:", gissning, "\n")
print("                         Rätta svaret:", slump, "\n")
#print("\n")
print("               ", end="")

print("\n")
print("                >>>>>    Du fick", points, "poäng!    <<<<<\n\n")
if (points >= 70):
    print("                          Snyggt jobbat!")
else:
    print("                 Bättre lycka nästa gång, kompis!")
print("\n")
