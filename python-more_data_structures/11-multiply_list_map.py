#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # We use list() to convert the map object back into a standard list.
    # lambda x: x * number is our instant, one-time-use function.
    return list(map(lambda x: x * number, my_list))
