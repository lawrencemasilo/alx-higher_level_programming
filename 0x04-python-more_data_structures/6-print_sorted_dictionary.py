#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    b_dictionary = a_dictionary.copy()
    sorted_dic = sorted(b_dictionary.keys())
    for key in sorted_dic:
        print("{}: ".format(key), end="")
        print("{}".format(b_dictionary[key]))
