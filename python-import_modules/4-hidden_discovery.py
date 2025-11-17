#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    #  dir() returns a sorted list of all names in the module
    names = dir(hidden_4)

    for name in names:
        #  only outputs if the first 2 characters are NOT "__"
        if name[:2] != "__":
            print(name)
