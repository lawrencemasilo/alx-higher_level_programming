#!/usr/bin/python3

def uniq_add(my_list=[]):
    temp_list = []
    result = 0
    for element in my_list:
        if element not in temp_list:
            result += element
            temp_list.append(element)
    return result
