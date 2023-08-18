#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    tuple_sum = 0
    avg = 0
    last_tuple = 0

    for element in my_list:
        last_tuple += element[1]
        tuple_sum += element[0] * element[1]
    if last_tuple == 0:
        return 0
    avg = tuple_sum / last_tuple
    return avg
