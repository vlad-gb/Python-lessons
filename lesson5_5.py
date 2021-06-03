#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from functools import reduce

# =================
print(">> Task 5")

CONST_NUMBERS_COUNT = 15


def write_arbitrary_numbers_to_file(file_out):
    try:
        with open(file_out, "w") as numbers_out_file:
            numbers_list_to_file = list()
            for i in range(CONST_NUMBERS_COUNT):
                numbers_list_to_file.append(str(randint(0, 23)))
            numbers_line_to_file = ' '.join(numbers_list_to_file)
            print(f"Writing arbitrary numbers to file: {numbers_out_file.name}")
            numbers_out_file.write(numbers_line_to_file)

    except IOError as e:
        print(f"Oops! got exception: {e}")

    return 0


def summing_numbers_from_file(file_in):
    numbers_list_sum = int(0)
    try:
        with open(file_in, "r") as numbers_in_file:
            numbers_str_list_from_file = numbers_in_file.readline()
            numbers_list_from_file = numbers_str_list_from_file.split()
            # Note: Another variant is using map() and sum() function instead of the reduce()
            numbers_list_sum = reduce(lambda x, y: int(x) + int(y), numbers_list_from_file)

    except IOError as e:
        print(f"Oops! got exception: {e}")

    return numbers_list_sum


file_for_numbers_store = "arbitrary_numbers_task_5.txt"
write_arbitrary_numbers_to_file(file_for_numbers_store)
print(f"Sum numbers from file: {file_for_numbers_store} is {summing_numbers_from_file(file_for_numbers_store)}")