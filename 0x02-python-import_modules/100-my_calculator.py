#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
        exit(1)
    else:
        a = argv[1]
        b = argv[3]
        operator = argv[2]
        if operator == '+':
            print("{} + {} = {}".format(a, b, add(int(a), int(b))), end="\n")
        elif operator == '-':
            print("{} - {} = {}".format(a, b, sub(int(a), int(b))), end="\n")
        elif operator == '*':
            print("{} * {} = {}".format(a, b, mul(int(a), int(b))), end="\n")
        elif operator == '/':
            print("{} / {} = {}".format(a, b, div(int(a), int(b))), end="\n")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
