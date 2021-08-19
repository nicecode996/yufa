# coding=utf-8
# !/usr/bin/env python3

# 创建全局变量
x = 1000

def print_value():
    print("函数中 x = {0}".format(x))

print_value()
print("全局变量x = {0}".format(x))

# 创建全局变量

def print_value():
    global x
    x = 10
    print("函数中x = {0}".format(x))

print_value()
print("全局变量 x = {0}".format(x))
