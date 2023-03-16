#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b == 0:
        return 1
    elif b < 0:
        n = b * -1
    else:
        n = b
    for i in range(n):
        if b < 0:
            result = result / a
        else:
            result = result * a
    return result
