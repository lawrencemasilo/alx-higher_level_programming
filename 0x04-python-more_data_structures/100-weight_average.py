#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    tuple_sum = 0
    avg = 0
    last_tuple = []

    for element in my_list:
        tuple_sum += element[0] * element[1]
        last_tuple.append(element[1])
    sum_2 = last_tuple[0] + last_tuple[1] + last_tuple[2] + last_tuple[3]
    if sum_2 == 0:
        return 0
    avg = tuple_sum / sum_2
    return avg
