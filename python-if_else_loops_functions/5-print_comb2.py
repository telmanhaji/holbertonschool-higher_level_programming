#!/usr/bin/python3
# This script prints numbers 0-99 with 2 digits and commas.

# We loop from 0 to 99 - thats why we use .
for i in range(100):
    #  Check if it is last number 99
    if i == 99:
        #  If it's 99, just the 2-digit number and a newline
        print(f"{i:02d}")
    else:
        #  For all other numbers with 2 digits,
        #  followed by a comma and a space.
        print(f"{i:02d}", end=", ")
