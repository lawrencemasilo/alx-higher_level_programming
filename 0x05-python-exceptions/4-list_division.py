#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    div_result = []
    for integer in range(list_length):
        try:
            if integer < len(my_list_1):
                int_1 = my_list_1[integer]
            else:
                int_1 = None
            if integer < len(my_list_2):
                int_2 = my_list_2[integer]
            else:
                int_2 = None

            if int_1 is None:
                raise IndexError("out of range")
            if int_2 is None:
                raise IndexError("out of range")
            try:
                float(int_1)
            except ValueError:
                raise TypeError("wrong type")
            try:
                int(int_1)
            except ValueError:
                raise TypeError("wrong type")
            try:
                float(int_2)
            except ValueError:
                raise TypeError("wrong type")
            try:
                int(int_2)
            except ValueError:
                raise TypeError("wrong type")

            if int_2 == 0:
                raise ZeroDivisionError("division by 0")
            div_result.append(int_1 / int_2)
        except ZeroDivisionError as ZD:
            print(ZD)
            div_result.append(0)
        except TypeError as TE:
            print(TE)
            div_result.append(0)
        except IndexError:
            print("out of range")
            div_result.append(0)
        finally:
            pass
    return div_result
