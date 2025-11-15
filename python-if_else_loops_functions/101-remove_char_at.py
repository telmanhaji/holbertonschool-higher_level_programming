#!/usr/bin/python3
# 101-remove_char_at.py - removes a character at a specific index.

def remove_char_at(str, n):
    new_string = ""
    for i in range(len(str)):
        if i != n:
            new_string = new_string + str[i]
    return new_string
