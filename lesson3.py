#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =================
print(">> Task 1")


def division(numerator, denominator):
    division_result = None
    try:
        division_result = numerator / denominator
    except ZeroDivisionError as e:
        print(f"Oops! got exception: {e}")
    return division_result


numerator_gained = 3
denominator_gained = 0
# numerator_gained = int(input("Please input numerator number:"))
# denominator_gained = int(input("Please input denominator number:"))

print(f"Result of division is: {division(numerator_gained, denominator_gained)}")

# =================
print(">> Task 2")


def put_user_info(first_name, middle_name, last_name, date_of_birth, city, email, phone):
    result_user_info = f"User: {first_name} {middle_name} {last_name}\n" \
                       f"Date of birth: {date_of_birth}\n" \
                       f"City: {city}\n" \
                       f"Email: {email}\n" \
                       f"Phone: {phone}"
    print(result_user_info)
    return


put_user_info(first_name="Alex", middle_name="Edwin", last_name="Smith",
              date_of_birth="10.11.1990", city="San Francisco",
              email="AlexEdwin@mail.com",
              phone="+79279179924")

# =================
print(">> Task 3")


def my_func(a, b, c):
    return sum([k for k in sorted((a, b, c))[1:]])


print(f"The sum of the two largest arguments is: {my_func(1, 2, 3)}")

# =================
print(">> Task 4")


def my_pow(x, y):
    temp = 1
    result = 1
    for k in range(abs(y)):
        temp *= x
    result = temp if y > 0 else 1 / temp
    return result


print(f"Three to the third power is: {my_pow(3, 4)}")
print(f"Three to the minus third power is: {my_pow(3, -4)}")

# =================
print(">> Task 5")


def rows_sum():
    raw_data = str()
    numbers_list = []
    result = 0
    is_exit = False
    while not is_exit:
        raw_data = input("Please input arbitrary row of numbers or symbol '*' for exit):")
        numbers_list = raw_data.split(" ")
        if '*' in numbers_list:
            end_pos = numbers_list.index('*')
            numbers_list = numbers_list[0:end_pos]
            is_exit = True
        result += sum(map(lambda n: int(n), numbers_list))
    return result


print(f"Sum of number's row is: {rows_sum()}")

# =================
print(">> Task 6")


def title_func(str):
    result_str = str.title()
    return result_str


print(f"Titled string: {title_func('abracadabra')}")

# =================
print(">> Task 7")

raw_data_str = "invia est in medicina via sine lingua latina"

data_str_splited_list = raw_data_str.split(" ")
data_str_titled_list = map(lambda str : title_func(str), data_str_splited_list)

result_data_str = ' '.join(data_str_titled_list)

print(f"Titled result string is: {result_data_str}")
