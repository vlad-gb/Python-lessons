#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =================
print(">> Task 3")


class Income:

    def __init__(self, wage, bonus):
        self.data = {"wage": wage, "bonus": bonus}

    def get_total_income(self):
        return self.data["wage"] + self.data["bonus"]


class Worker:

    def __init__(self, name, surname, position_, income):
        self.name = name
        self.surname = surname
        self.position = position_
        self._income = income


class Position(Worker):

    def __init__(self, name, surname, position_, income):
        super().__init__(name, surname, position_, income)

    def get_full_name(self):
        print(f"Worker's full name: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Worker's total income: {self._income.get_total_income()}")


worker_position = Position("James", "Cameron", "student", Income(3000, 500))
worker_position.get_full_name()
worker_position.get_total_income()

print("It's all done")
