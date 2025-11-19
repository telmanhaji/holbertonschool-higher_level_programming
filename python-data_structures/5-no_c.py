#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all characters c and C from a string.
    """
    # 1st. Creates an empty bucket to hold the clean characters
    new_string = ""

    # 2nd. Loops through every single character in the input string
    for char in my_string:
        # 3rd. Checks: If the character is NOT 'c' AND NOT 'C'
        if char != 'c' and char != 'C':
            # 4th. It is safe to add to our new string
            new_string += char

    # 5th. Returns the fully constructed clean string
    return new_string
