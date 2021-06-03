#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import mean

# =================
print(">> Task 3")

CONST_SALARY_THRESHOLD = 20000.0


def get_analytics_staff_info_from_file(file_name):
    try:
        with open(file_name, "r") as user_file:
            staff_salary_list = list()
            print(f"The employees who gets paid more then {CONST_SALARY_THRESHOLD}:")
            print("---------------------------------------------------------")
            print(f"{'Name'.ljust(15)} | {'Salary'}")
            print("---------------------------------------------------------")
            for staff_file_line in user_file:
                if staff_file_line == "":
                    break
                staff_info = staff_file_line.split()
                staff_salary_list.append(float(staff_info[2]))
                if float(staff_info[2]) > CONST_SALARY_THRESHOLD:
                    print(f"{staff_info[1].ljust(15)} | {staff_info[2]}")
            average_salary = mean(staff_salary_list)
            print("---------------------------------------------------------")
            print(f"Average salary of the department is {average_salary}")
    except IOError as e:
        print(f"Oops! got exception: {e}")
    return 0


get_analytics_staff_info_from_file("staff_info_task_3.txt")