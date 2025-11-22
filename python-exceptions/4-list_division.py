#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    This module divides element by element 2 lists.
    Handles errors gracefully.
    """
    new_list = []

    # 1st. it loops exactly 'list_length' times, as requested.
    for i in range(list_length):
        try:
            # assume success first
            result = 0

            # 2nd. the dangerous operation
            # this line can fail in 3 different ways:
            # - my_list_1[i] or my_list_2[i] doesn't exist (IndexError)
            # - they are not numbers (TypeError)
            # - my_list_2[i] is 0 (ZeroDivisionError)
            result = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            print("division by 0")
            result = 0

        except TypeError:
            print("wrong type")
            result = 0

        except IndexError:
            print("out of range")
            result = 0

        finally:
            # 3rd. the cleanup / commit
            # whether the math worked or failed, we MUST add an entry
            # (either the answer or 0) to keep the list length correct.
            new_list.append(result)

    return new_list
