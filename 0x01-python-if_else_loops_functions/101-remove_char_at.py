#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    str_copy = ""
    if ((n < len(str)) and (n >= 0)):
        for i in str:
            if (i != str[n]):
                str_copy += i
    elif (n > len(str) and (n >= 0)):
        str_copy = str
    else:
        str_copy = str
    return str_copy
