#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =================
print(">> Task 2")


def get_word_and_line_count_in_file(file_name):
    try:
        with open(file_name, "r") as user_file:
            line_number = 0
            for user_file_line in user_file:
                word_count_in_line = len(user_file_line.split())
                line_number += 1
                print(f"Word count in line {line_number} is: {word_count_in_line}")
            print("----------------------------------------------------------")
            print(f"Total count of lines in file {user_file.name} is {line_number}")
    except IOError as e:
        print(f"Oops! got exception: {e}")
    return 0


get_word_and_line_count_in_file("text_file_for_task_2.txt")