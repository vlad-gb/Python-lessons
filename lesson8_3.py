#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =================
print(">> Task 3")


class DelimiterError(Exception):
    def __init__(self, txt):
        self.txt = txt


def input_validated_numbers():
    raw_data = str()
    validated_numbers_list = []
    is_exit = False
    while not is_exit:
        raw_data = input("Please input arbitrary row of numbers or symbol '*' for exit:")
        numbers_list_str = raw_data.split(" ")
        for number_str in numbers_list_str:
            if number_str in ['', ' ', '\t']:
                raise DelimiterError("ExtraCharactersError: invalid delimiter between numbers")
            if number_str == '*':
                is_exit = True
                break
            try:
                number_int = int(number_str)
            except ValueError as e:
                print(f"Oops! Got exception: {e}")
            except DelimiterError as e:
                print(f"Oops! Got exception: {e}")
            else:
                validated_numbers_list.append(number_int)
    return validated_numbers_list


numbers_list = input_validated_numbers()

print(f"Inputs validated numbers list is: {numbers_list}")

print("It's all done")
