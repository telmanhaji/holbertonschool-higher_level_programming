#!/usr/bin/python3
# 100-print_tebahpla.py - displays the reverse, alternating alphabet.

for i in range(122, 96, -1):
    if i % 2 == 0:
        char_num = i
    else:
        char_num = i - 32
    print("{:c}".format(char_num), end="")
