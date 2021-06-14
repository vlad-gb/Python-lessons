#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

# =================
print(">> Task 1")


class Data:

    data_str = ""
    last_error = ""

    def __init__(self, data_str):
        """Argument 'data_str' has followed format: 'day-month-year'"""
        Data.data_str = data_str

    @classmethod
    def parse(cls):
        try:
            datetime_object = datetime.strptime(cls.data_str, '%d-%m-%Y')
        except ValueError as e:
            cls.last_error = str(e)
            return None
        return f"{int(datetime_object.day)}-{int(datetime_object.month)}-{int(datetime_object.year)}"

    @staticmethod
    def get_last_error():
        if Data.last_error != "":
            return f"Data parsing failed: {Data.last_error}"
        else:
            return None


formatted_data = Data("10-13-2001").parse()

if formatted_data:
    print(f"Data is: {formatted_data}")
else:
    print(Data.get_last_error())

print("It's all done")
