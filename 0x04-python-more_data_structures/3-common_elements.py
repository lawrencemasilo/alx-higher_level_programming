#!/usr/bin/python3

def common_elements(set_1, set_2):
    for element in set_2:
        if element in set_1:
            return set(element)
        else:
            continue
