#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

# =================
print(">> Task 4,5,6")


class Storage:
    """Singleton class"""
    staff_count = 0
    staff_list = []

    def __init__(self):
        pass

    @staticmethod
    def add_staff(staff):
        print(staff.get_info())
        Storage.staff_list.append(staff)
        Storage.staff_count += 1
        print(f"Added {staff.get_info()} to storage(now total: {Storage.staff_count})")

    @staticmethod
    def pass_to_customer(staff, company_division):
        if staff in Storage.staff_list:
            Storage.staff_list.remove(staff)
            Storage.staff_count -= 1
            staff.company_division = company_division
            print(f"{staff.get_info()} passed to company division: {staff.company_division}")
        else:
            print(f"Failure: There is no the {staff.get_info()} in stock")


class OfficeEquipment(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def get_info(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, price, model):
        super().__init__(price)
        self.model = model
        self.company_division = None

    def get_info(self):
        return f"Printer(model: {self.model}, price: {self.price})"


printer = Printer(100, "Canon")
Storage.add_staff(printer)
Storage.pass_to_customer(printer, "Sales department")
Storage.pass_to_customer(printer, "Sales department")

print("It's all done")
