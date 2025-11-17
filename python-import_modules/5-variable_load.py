#!/usr/bin/python3
"""
This module imports a secret from another file and outputs it.
"""

if __name__ == "__main__":
    # 1. Import the variable 'a' specifically
    #    Syntax: from [filename_without_py] import [variable_name]
    from variable_load_5 import a

    # 2. Print the variable
    #    Once imported, 'a' works just like a variable you defined yourself.
    print(a)
