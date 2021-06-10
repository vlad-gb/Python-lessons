#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil
from abc import ABC, abstractmethod

# =================
print(">> Task 2")


class Clothes(ABC):
    @abstractmethod
    def model(self):
        pass

    @abstractmethod
    def calculate_fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, model, size):
        self.m = model
        self.V = int(size)

    @property
    def size(self):
        print(f"Coat's size is {self.V}")
        res = format(self.V, '3,d')
        return res

    @property
    def model(self):
        print(f"Coat's model is {self.m}")
        return self.m

    def calculate_fabric_consumption(self):
        res = self.V / 6.5 + 0.5
        fress = format(float(ceil(res * 100) / 100), '~>4,.2f')  # round float to the largest previous
        return fress


class Suit(Clothes):
    def __init__(self, model, height):
        self.m = model
        self.H = int(height)

    @property
    def height(self):
        print(f"Coat's height is {self.H}")
        res = format(self.H, '3,d')
        return res

    @property
    def model(self):
        print(f"Coat's model is {self.m}")
        return self.m

    def calculate_fabric_consumption(self):
        res = 2 * self.H + 0.3
        fress = format(float(ceil(res * 100) / 100), '~>4,.2f')  # round float to the largest previous
        return fress


coat = Coat("Chesterfield", 50)
print(f"To make a coat of the \'{coat.model}\' model and size {coat.size}"
      f"needed {coat.calculate_fabric_consumption()} meters of fabric ")

print("It's all done")
