#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    iterator = 0
    for arg in argv:
        if (len(argv) == 1):
            print("0 arguments.")
        elif (len(argv) > 1) and (iterator != 0):
            if len(argv) == 2:
                print("1 argument:")
            elif (len(argv) > 2) and (iterator == 1):
                print("{} arguments:".format(len(argv) - 1), end="\n")
            print("{}: {}".format(iterator, arg), end="\n")
        iterator += 1
