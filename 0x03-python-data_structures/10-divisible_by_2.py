#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list:
        new_list = my_list.copy()
        for element in new_list:
            if element % 2 == 0:
                return (new_list, True)
            else:
                return (new_list, False)
