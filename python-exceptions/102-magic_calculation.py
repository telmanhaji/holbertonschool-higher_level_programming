#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                # note: the bytecode for the math starts at offset 58.
                # the IF check jumps to 58 if False.
                # so the math happens if the exception is NOT raised.
                result += (a ** b) / i
        except Exception:
            result = b + a
            break
    return result
