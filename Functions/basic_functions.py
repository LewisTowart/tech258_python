# Functions

# DRY - Don't Repeat Yourself

# function with no arguments

# def print_something(name):
#     print("Hello my name is? " + name)
#
# print_something("Lewis")
#
# # function with args
#
# def addition(int1, int2):
#     return int1 + int2
#
#
# print(addition(2, 2))
# print(addition(25, 20))

# default arguments

# def addition(int1=2, int2=2):
#     return int1 + int2
#
# print(addition())
# print(addition(2, 6))

# multiple arguments

# def multi_args(*multiargs):
#     for arg in multiargs:
#         print(arg)
#
# multi_args(1, 2, 3, 4, 5)

# type hints

# def division(denom: int, num: int) -> float:
#     return denom / num
#
# print(division(5, 3))
