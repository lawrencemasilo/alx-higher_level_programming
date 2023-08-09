#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_number = number % -10
else:
    last_number = number % 10
if last_number > 5:
    str_con = "and is greater than 5"
elif last_number == 0:
    str_con = "and is 0"
else:
    str_con = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_number} {str_con}")
