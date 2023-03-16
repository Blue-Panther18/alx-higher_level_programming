#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b == 0:
        return 1
    elif b < 0:
        b = b * -1
        a = 1 / a
    for i in range(b):
        result = result * a
        if a < 0 and b % 2 == 1:
            return -result
    return result
