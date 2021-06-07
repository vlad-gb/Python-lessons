#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =================
print(">> Task 4")


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        pass

    def stop(self):
        pass

    def turn(self, direction):
        pass

    def show_speed(self):
        print(f"Car speed is {self.speed}")


class TownCar(Car):

    def show_speed(self):
        if self.speed < 60.0:
            super().show_speed()
        else:
            print(f"Speed limit exceeded!")


townCar = TownCar(70, "Red", "Maserati", True)
townCar.show_speed()

print("It's all done")
