#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =================
print(">> Task 2")


class Road:
    weight_per_square_meter = 1.25  # kg per m^2

    def __init__(self, length=0, width=0):
        self._length = length
        self._width = width

    def weight_calculate(self):
        """Calculation of asphalt mass in ton"""
        result_weight = self._length * self._width * Road.weight_per_square_meter / 1000.0
        return result_weight


road = Road(length=5000, width=20)

print(f"Asphalt mass is {road.weight_calculate()} ton")

print("It's all done")
