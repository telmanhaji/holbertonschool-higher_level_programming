#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    This module raises a NameError exception with a message.
    """
    # it raises the NameError, but it passes the 'message' variable into it.
    # this stores the text inside the error object.
    raise NameError(message)
