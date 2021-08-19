# coding=utf-8
# !/usr/bin/env python3
'''
def square(num):  # 定义函数
    n_list = []

    for i in range(1, num + 1):  # 通过循环计算一个数的平方
        n_list.append(i * i)  # 值保存在列表中

    return n_list  # 返回列表对象


for i in square(10):  # 遍历所有的列表对象
    print(i, end=' ')
'''


# 改良方案
def square(num):
    for i in range(1, num + 1):
        yield i * i  # yieid关键字返回平方数

# 此处使用的隐式调用，显式调用相对复杂，此处不使用
for i in square(5):  # 生成器是一种可迭代对象，可迭代对象通过_next_()方法获得元素，此行代码能够遍历可迭代对象，就是隐式调用生成器的_next_()方法获得元素的
    print(i, end=' ')
