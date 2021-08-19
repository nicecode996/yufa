# coding=utf-8
# !/usr/bin/env python3

def calculate_fun(opr):
    if opr == '+':
        return lambda a, b: (a + b)
    else:
        return lambda a, b: (a - b)


f1 = calculate_fun('+')
f2 = calculate_fun('-')

print(type(f2))

print("10 + 5 = {0}".format(f1(10, 5)))
print("10 - 5 = {0}".format(f2(10, 5)))
