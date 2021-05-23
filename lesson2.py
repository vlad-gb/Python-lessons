#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=================
print(">> Task 1")


class Animal:
    def __init__(self, species):
        self.species = species


cat = Animal("Cat")

some_list = [None, 7, 3.14, complex(3, 4), "text", [1, 2, 3], Animal, cat]

for it in some_list:
    if isinstance(it, type(None)):
        print(f"Variable {it} is None")
    elif isinstance(it, int):
        print(f"Variable {it} is int")
    elif isinstance(it, float):
        print(f"Variable {it} is float")
    elif isinstance(it, complex):
        print(f"Variable {it} is complex")
    elif isinstance(it, str):
        print(f"Variable {it} is str")
    elif isinstance(it, list):
        print(f"Variable {it} is list")
    elif isinstance(it, type):
        print(f"Variable {it} is class")
    elif isinstance(it, object):
        print(f"Variable {it} is object")

#=================
print(">> Task 2")

#list_task2 = input("Please input list's items:").split()

list_task2 = [1, 2, 3, 4, 5, 6, 7]

print(f"Init list: {list_task2}")

list_len = 2 * (len(list_task2) // 2)
print(list_len)
list_task2[:list_len:2], list_task2[1:list_len:2] = list_task2[1:list_len:2], list_task2[:list_len:2]

print(f"Output list: {list_task2}")

#=================
print(">> Task 3")

month_num = 3
#month_num = int(input("Please input arbitrary month number(1..12):"))

months_dict = {
    1: "January", 2: "February",
    3: "March", 4: "April", 5: "May",
    6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November",
    12: "December"
}

seasons_list_map = [
    None, 1, 1, #Winter
    2, 2, 2,  #Spring
    3, 3, 3,  #Summer
    4, 4, 4,  #Autumn
    1         #Winter
]

seasons_list_val = [None, "Winter", "Spring", "Summer", "Autumn"]

season_from_list = seasons_list_val[seasons_list_map[month_num]]
print(f"From list: {months_dict.get(month_num)} is a {season_from_list}")

seasons_dict_map = {
    12: 1, 1: 1,  2: 1,  #Winter
    3: 2,  4: 2,  5: 2,  #Spring
    6: 3,  7: 3,  8: 3,  #Summer
    9: 4,  10: 4, 11: 4 #Autumn
}

seasons_dict_val = {1: "Winter", 2: "Spring", 3: "Summer", 4: "Autumn"}

season_from_dict = seasons_dict_val[seasons_dict_map[month_num]]
print(f"From dict: {months_dict.get(month_num)} is a {season_from_dict}")

#=================
print(">> Task 4")

init_str = "Mercury8901234 Venus678901234 Earth Mars Jupiter Saturn Uranus Neptune"
planets_list = init_str.split(" ")
for i, val in enumerate(planets_list):
    print(f"Planet number {i+1} is {val[:10]}")

#=================
print(">> Task 5")

ranking_list = [7, 5, 3, 3, 2]

new_rank_num = 5
#new_rank_num = int(input("Please input arbitrary rank number:"))
index_to_insert = 0

for i, val in enumerate(ranking_list):
    print(f"{i}:{val}")
    if val < new_rank_num:
        index_to_insert = i
        break

ranking_list.insert(index_to_insert, new_rank_num)

print(f"Output list: {ranking_list}")

#=================
print(">> Task 6")

Items = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

#1. Converting items info to analytiсal data

attribute_dict = dict()

for it in Items:
    print(f"Item number {it[0]} has attributes:")
    for key, val in it[1].items():
        print(f"   {key}:{val}")
        if not(key in attribute_dict):
            attr_value_set = set()
            attr_value_set.add(val)
            attribute_dict[key] = attr_value_set
        else:
            attribute_dict[key].add(val)

#2. Refactoring analytiсal data(set -> list)

for key, attr_value_set in attribute_dict.items():
    attr_value_list = list(attr_value_set)
    attribute_dict[key] = attr_value_list

print(f"Resulting analitycal data:\n {attribute_dict}")
