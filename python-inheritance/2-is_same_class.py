#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class;
    otherwise False.
    """
    # it compares the type of the object directly to the class.
    # it does NOT use isinstance() because that allows inheritance.
    return type(obj) == a_class
