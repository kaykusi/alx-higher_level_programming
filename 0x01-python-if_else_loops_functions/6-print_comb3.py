#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if x == 8 and y == 9:
            print("89")
        elif x < y:
            print("{0:d}{1:d}, ".format(x, y), end="")
