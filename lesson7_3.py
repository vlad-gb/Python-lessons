#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =================
print(">> Task 3")


class Cell:
    def __init__(self, subcells_count):
        self.subcells_count = subcells_count

    def __str__(self):
        return f"Object cell with {self.subcells_count} subcells"

    @staticmethod
    def make_order(some_cell, row_count):

        subcells_row_count, subcells_row_remains = divmod(some_cell.subcells_count, row_count)
        res_list = [''.ljust(row_count, '*') for i in range(subcells_row_count)]
        if subcells_row_remains > 0:
            remain_row = "".ljust(subcells_row_remains, '*')
            remain_row += "".ljust(row_count - subcells_row_remains, '0')
            res_list.append(remain_row)
        res_str = '\n'.join(res_list)
        print(f"Ordered subcells:\n{res_str}")

    def __add__(self, other_cell):

        res_subcells_count = self.subcells_count + other_cell.subcells_count
        res_cell = Cell(res_subcells_count)

        return res_cell

    def __sub__(self, other_cell):
        res_subcells_count = self.subcells_count - other_cell.subcells_count if self.subcells_count - other_cell.subcells_count > 0 else 0
        res_cell = Cell(res_subcells_count)
        return res_cell

    def __mul__(self, other_cell):
        res_subcells_count = self.subcells_count * other_cell.subcells_count
        res_cell = Cell(res_subcells_count)
        return res_cell

    def __truediv__(self, other_cell):
        res_subcells_count = self.subcells_count // other_cell.subcells_count
        res_cell = Cell(res_subcells_count)
        return res_cell


cell_1 = Cell(16)
print(f"Cell 1: {cell_1}")
cell_2 = Cell(5)
print(f"Cell 2: {cell_2}")

cell_3 = cell_1 + cell_2
print(f"Sum of cell_1 and cell_2 is {cell_3}")

Cell.make_order(cell_3, 5)

print("It's all done")
