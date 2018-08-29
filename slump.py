#!/usr/local/bin/python
# coding: utf-8
import random

# Första ver:
slump = 0
x = 0
while(slump != 20):
    slump = random.randrange(0,100)
    x = x + 1
print("\n\n",x,"\n\n")

# Nästan "One-liner":
x=0
while(random.randrange(0,100)!= 20):
    x = x + 1
print(x)
