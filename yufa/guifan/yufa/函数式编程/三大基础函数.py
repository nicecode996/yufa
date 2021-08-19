# coding=utf-8
# !/usr/bin/env python3

# 语法格式
# filter(function,iterable) # function这是一个函数   iterable 这是一个可迭代对象

# 过滤函数
users = ['Tony', 'Tom', 'Ben', 'Alex']

users_filter = filter(lambda u: u.startswith('B'), users)  # 如果为True则保留，False的元素被过滤掉 ，过滤B开头
print(list(users_filter))

# 实现了1-10的偶数
number_list = range(1, 11000)
number_filter = filter(lambda it: it % 50 == 0, number_list)
print(list(number_filter))
print(type(number_filter))
print(type(users))

# 映射函数 map
# 语法格式 map(function,iterable)

users = ['Tony', 'Tom', 'Ben', 'Aelx']

users_map = map(lambda u: u.lower(), users)  # 将四个名字转换成小写字母
print(list(users_map))

# 先使用filter函数过滤在使用map函数进行转换

users = ['Tony', 'Tom', 'Ben', 'Aelx']

users_filter = filter(lambda u: u.startswith('T'), users)  # 冒号前面的u是lambda参数列表 冒火后面的u是lambda体

# users_map = map(lambda u:u.lower(),users_filter)
users_map = map(lambda u: u.lower(), filter(lambda u: u.startswith('T'), users))
print(list(users_map))

# 聚合函数
# 语法格式： reduce(function, iterable[, initializer])   参数function是聚合操作函数，该函数有两个参数，
# 参数iterable是可迭代对象，参数inITializer是初始值

from functools import reduce  # reduce是在functools模块中定义的，这一步是导入functools模块

a = (1, 2, 3, 4)
a_reduce = reduce(lambda acc, i: acc + i, a)  # 10
# 调用reduce()函数,其中lambda acc，i是进行聚合操作的lambda表达式，
# 有两个参数，其中acc是上次累计计算结果 i是当前元素，acc + i表达式是进行累加。
# a_reduce = redece(lambda acc, i: acc + i, a, 2) # 12是运行结果   2是运行初始值
print(a_reduce)
