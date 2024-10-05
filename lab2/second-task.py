#!/usr/bin/python3

from sys import stderr, stdin
import re


try:
    for line in stdin:
        try:
            name = line.strip()
            
            if not name[0].isupper():
                raise Exception("Name needs to start in uppercase!")
            if not bool(re.match(r"^[A-Za-z]+$", name)):
                raise Exception("Invalid letters!")

            print(f"Nice to see you {name}!")
        except Exception as e:
            print(f"Error: {str(e)}", file=stderr)
except KeyboardInterrupt:
    print("\nGoodbye!")
