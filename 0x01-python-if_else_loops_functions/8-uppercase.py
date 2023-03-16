#!/usr/bin/python3
def uppercase(str):
    result = ''
    for ch in str:
        n = ord(ch)
        if n > 96 and n < 123:
            result += "{:c}".format(n-32)
        else:
            result += "{:c}".format(n)
    print(result)
