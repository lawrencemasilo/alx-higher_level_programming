#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if (my_list):
        index = -1
        while index >= (len(my_list) * -1):
            print("{:d}".format(my_list[index]))
            index -= 1
