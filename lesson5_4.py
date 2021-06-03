#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =================
print(">> Task 4")

numerals_dict = {"One": "Odin", "Two": "Dva", "Three": "Tri", "Four": "Chetyre"}


def convert_english_numerals_to_russian(file_in, file_out):
    russian_numerals_all_lines = list()
    try:
        with open(file_in, "r") as numbers_in_file:
            print(f"Reading from init file: {numbers_in_file.name}")
            english_numerals_all_lines = numbers_in_file.readlines()
            print("English numerals converting to russian...")
            for english_numeral_line in english_numerals_all_lines:
                english_numeral_line_list = english_numeral_line.split()
                english_numeral_line_list[0] = numerals_dict[english_numeral_line_list[0]]
                russian_numerals_all_lines.append(' '.join(english_numeral_line_list) + '\n')
    except IOError as e:
        print(f"Oops! got exception: {e}")

    try:
        with open(file_out, "w") as numbers_out_file:
            print(f"Writing to out file: {numbers_out_file.name}")
            numbers_out_file.writelines(russian_numerals_all_lines)
    except IOError as e:
        print(f"Oops! got exception: {e}")

    print("It's all done")
    return 0


convert_english_numerals_to_russian("english_numerals_task_4.txt", "russian_numerals_task_4.txt")
