#!/usr/bin/python3
def uppercase(str):
    upper_case = ""
    for char in str:
        if ord(char) in range(ord('a'), ord('z') + 1):
            upper = chr(ord(char) - 32)
            upper_case = upper_case + upper
        else:
            upper_case = upper_case + char
    print("{}".format(upper_case), end="\n")
