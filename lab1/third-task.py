#!/usr/bin/python3

from math import sqrt
from sys import stderr


try:
    inp = float(input())

    if inp < 0:
        raise Exception

    with open("output.txt", "a") as f:
        print(sqrt(inp), file=f)
except Exception as e:
    print("Error: " + str(e), file=stderr)
    exit(1)
