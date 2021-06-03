#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =================
print(">> Task 6")

CONST_NUMBERS_COUNT = 15


def calculation_total_hours_of_disciplines(file_in):
    numbers_list_sum = int(0)

    def raw_hours_str_handle(raw_str):
        if raw_str == '—':
            return 0
        elif '(' in raw_str:
            end_pos = raw_str.index('(')
            hours = int(raw_str[0:end_pos])
            return hours
        return 0

    try:
        with open(file_in, "r") as lecture_table_file:
            for line in lecture_table_file:
                if ':' in line:
                    lecture_name, lecture_hours = line.split(':')
                    lecture_hours_raw_list = lecture_hours.split()
                    lecture_hours_list = map(lambda x: raw_hours_str_handle(x), lecture_hours_raw_list)
                    lecture_hours_sum = sum(lecture_hours_list)
                    print(f"Total hours of lecture {lecture_name} are {lecture_hours_sum}")

    except IOError as e:
        print(f"Oops! got exception: {e}")

    return 0


calculation_total_hours_of_disciplines("text_file_for_task_6.txt")
print("It's all done")