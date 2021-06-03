#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =================
print(">> Task 1")


def get_write_user_data_to_file():
    with open("user_info_task1.txt", "w") as user_file:
        while True:
            user_string = input("Please input arbitrary string or empty input for exit: ")
            if user_string == "":
                break
            user_string += "\n"
            user_file.write(user_string)
    return 0


get_write_user_data_to_file()