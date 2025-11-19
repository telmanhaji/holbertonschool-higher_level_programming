#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list and returns a list
     of booleans.
    """
    # Using a technique called List Comprehension.
    # It loops through the old list and creates a new one in a single line.

    # The new element will be (num % 2 == 0) for every 'num' in 'my_list'.
    # Python automatically evaluates (num % 2 == 0) to True or False.
    new_list = [(num % 2 == 0) for num in my_list]

    return new_list
