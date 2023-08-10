#!/usr/bin/python3
for firstInteger in range(10):
    for secondInteger in range(firstInteger + 1, 10):
        if (firstInteger != 8) and (secondInteger != 9):
            print("{}{},".format(firstInteger, secondInteger), end=" ")
        elif (firstInteger == 8) and (secondInteger == 9):
            print("{}{}".format(firstInteger, secondInteger), end=" ")
        else:
            print("{}{},".format(firstInteger, secondInteger), end=" ")
