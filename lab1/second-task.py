#!/usr/bin/python3

from math import inf
from sys import stderr, exit
from random import randint


try:
    A = float(input())
    
    B = randint(-10, 10)
    if B == 0:
        raise Exception

    print(A / B)
    
except Exception as exp:
    print("Error: " + str(e), file=stderr)
    exit(1)
