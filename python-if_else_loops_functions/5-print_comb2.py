#!/usr/bin/python3
# This script prints numbers 0-99 with 2 digits and commas.

for i in range(100):
    if i == 99:
        print(f"{i:02d}")
    else:
        print(f"{i:02d}", end=", ")
