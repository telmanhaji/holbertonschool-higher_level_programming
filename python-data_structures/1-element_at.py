#!/usr/bin/python3

def element_at(my_list, idx):
    """ Return element at given idx """
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
