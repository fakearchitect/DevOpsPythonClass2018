#!/usr/local/bin/python
# coding: utf-8
import os

'''
    Foreground colors
       30    Black
       31    Red
       32    Green
       33    Yellow
       34    Blue
       35    Magenta
       36    Cyan
       37    White

    Background colors
       40    Black
       41    Red
       42    Green
       43    Yellow
       44    Blue
       45    Magenta
       46    Cyan
       47    White
'''

# '\33[0m'
# '\033[33m'

# (u"\u2554") + ╔
# (u"\u255A") + ╚
# (u"\u2557") + ╗
# (u"\u255D") + ╝
# (u"\u2566") + ╦
# (u"\u2569") + ╩
# (u"\u2551") + ║
# (u"\u2550") + ═
# (u"\u2560") + ╠
# (u"\u2563") + ╣
# (u"\u256C") + ╬

os.system("clear")
theLinesX = 5
columnHeads = ["ADAM", "BERTIL", "CEASAR", "DAVID", "ERIK", "FREDRIK", "GUSTAV"]
theColumnsY = len(columnHeads)
content=" + "

def contents(X,Y):
    if X == 0:
        cont = columnHeads[Y] # På första raden, fyll i rubrikerna
    else:
        cc = (str(len(columnHeads[Y])) * len(columnHeads[Y] ) ) # Alla andra rutor fylls med antal tecken i rubriken.
        contW = len(columnHeads[Y])
        cont = cc + ((" ") * (abs(len(cc)-contW))) # fyll på med skillnaden i spaces
    return cont;

def coloring(X,Y):
    color = ("\033[" + str(Y+31) + "m")
    return color;

# Första raden:
print("\n" + (u"\u2554") + ((u"\u2550")*len(columnHeads[0])), end="") # ╔ / ═
for i in range(theColumnsY-1):
    print((u"\u2566") + ((u"\u2550")*len(columnHeads[i+1])), end="") # ╦ / ═
print((u"\u2557"), end="")  # ╗

# Resten:
for x in range (theLinesX):
    print("\n", end="")
    for y in range (theColumnsY):
        print((u"\u2551"), end="")   # ║
        print(coloring(x, y) + contents(x, y) + "\33[0m", end="")
    print((u"\u2551"), end="")  # ║
    if(x<(theLinesX-1)):
        print("\n" + (u"\u2560") + ((u"\u2550")*len(columnHeads[0])), end="") # ╠ / ═
        for i in range(theColumnsY-1):
            print((u"\u256C") + ((u"\u2550")*len(columnHeads[i+1])), end="") # ╬ ═ ═ ═
        print((u"\u2563"), end="")                                              # ╣
    else:
        print("\n" + (u"\u255A") + ((u"\u2550")*len(columnHeads[0])), end="") # ╚ ═
        for i in range(theColumnsY-1):
            print((u"\u2569") + ((u"\u2550")*len(columnHeads[i+1])), end="") # ╩ ═ ═ ═
        print((u"\u255D"), end="") # ╝


print("\n\n\n")
