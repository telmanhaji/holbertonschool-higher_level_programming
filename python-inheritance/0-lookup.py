#!/usr/bin/python3
"""
this module defines a function for object introspection.
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object.

    args:
        obj (any): The object to inspect.

    returns:
        list: a list of strings representing the attributes and methods.
    """
    # dir() is a built-in function that returns a list of
    # valid attributes for the object passed to it.
    return dir(obj)
