#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        count = 0
        for value in my_list:
            if i < x:
                print(value, end="")
                count += 1
                i += 1
        print(end="\n")
        return int(count)
    except IndexError:
        pass
