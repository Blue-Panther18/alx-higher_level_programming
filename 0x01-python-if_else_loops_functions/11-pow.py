#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b == 0:
        return 1
    elif b < 0:
        n = b * -1
    else:
        n = b
    if a < 0:
        p = a * -1
    else:
        p = a
    for i in range(n):
        if b < 0:
            result = result / p
        else:
            result = result * p
        if a < 0 and n % 2 == 1:
            result = result * -1
    return result
