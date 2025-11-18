#!/usr/bin/python3

def print_list_integer(my_list=[]):
    # loop each item in list
    for i in my_list:
        # ':d' format specifier ensures it`s outputs as a decimal integer
        print("{:d}".format(i))
