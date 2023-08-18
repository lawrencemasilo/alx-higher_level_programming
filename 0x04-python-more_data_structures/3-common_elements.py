#!/usr/bin/python3

def common_elements(set_1, set_2):
    word = set()
    for element in set_2:
        if element in set_1:
            word.add(element)
        else:
            continue
    return word
