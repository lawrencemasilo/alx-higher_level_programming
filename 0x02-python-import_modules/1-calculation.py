#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)), end="\n")
    print("{} - {} = {}".format(a, b, sub(a, b)), end="\n")
    print("{} * {} = {}".format(a, b, mul(a, b)), end="\n")
    print("{} / {} = {}".format(a, b, div(a, b)), end="\n")
