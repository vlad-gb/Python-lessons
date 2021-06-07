#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

# =================
print(">> Task 5")


class Stationery(ABC):
    @abstractmethod
    def draw(self):
        pass


class Pen(Stationery):
    title = "Pen"

    def draw(self):
        print(f"Start drawing of object of the class '{Pen.title}' that is instance of the parent class 'Stationery'")


class Pencil(Stationery):
    title = "Pencil"

    def draw(self):
        print(f"Start drawing of object of the class '{Pencil.title}' that is instance of the parent class 'Stationery'")


class Handle(Stationery):
    title = "Handle"

    def draw(self):
        print(f"Start drawing of object of the class '{Handle.title}' that is instance of the parent class 'Stationery'")


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()

print("It's all done")
