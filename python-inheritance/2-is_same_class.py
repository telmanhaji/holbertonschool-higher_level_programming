#!/usr/bin/python3
"""
this module defines a function for strict type checking.
it is used to verify if an object is exactly an instance of a class.
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class;
    otherwise False.

    args:
        obj (any): the object to check.
        a_class (type): The class to match against.

    returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
