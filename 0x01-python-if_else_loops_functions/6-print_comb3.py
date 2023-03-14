#!/usr/bin/python3
for n in range(10):
    for i in range(10):
        if n != i and i > n:
            print("{}{}".format(n, i), end="")
            if n != 8:
                print(", ", end="")
print("")
