#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        highest = 0
        h_key = ""
        for key in a_dictionary:
            if a_dictionary[key] > highest:
                highest = a_dictionary[key]
                h_key = key
            else:
                continue
        return h_key
    else:
        return None
