# coding=utf-8
# !/usr/bin/env python3

def sum( *numbers, multiple=1):
    total = 0.0
    for numbers in numbers:
        total += number
    return total * multiple


print(sum(100.0,20.0,30.0))
print(sum(30.0,80.0))
print(sum(30.0,80.0,multiple=2))


def double_tuple(param, param1, param2):
    pass


double_tuple (50.0,60.0,0.0)
print(sum(30.0,80.0,*double_tuple))


