#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =================
print(">> Task 2")


class DivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


def division(numerator, denominator):
    division_result = None
    try:
        if denominator == 0:
            raise DivisionError("Denominator is equal 0")
    except DivisionError as e:
        print(f"Oops! got exception: {e}")
    else:
        return float(numerator / denominator)
    return None


numerator_gained = int(input("Please input numerator number:"))
denominator_gained = int(input("Please input denominator number:"))

print(f"Result of division is {division(numerator_gained, denominator_gained)}")

print("It's all done")
