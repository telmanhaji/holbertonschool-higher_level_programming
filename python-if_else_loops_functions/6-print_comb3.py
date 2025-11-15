#!/usr/bin/python3
# This script displays all unique 2-digit combinations.

for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print(f"{i}{j}")
        else:
            print(f"{i}{j}", end=", ")
