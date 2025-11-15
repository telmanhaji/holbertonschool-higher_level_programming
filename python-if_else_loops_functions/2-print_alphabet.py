#!/usr/bin/python3
# This script loops through ASCII numbers 97-122
# and prints their character values.

for i in range(97, 123):
    #  chr(i) turns the number (e.g., 97) into a letter ('a')
    #  end="" prints it without a new line, so they all
    #  appear on the same line.
    print(chr(i), end="")