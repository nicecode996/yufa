# coding=utf-8
# !/usr/bin/env/python3

class Animal(object):
    """"定义动物类"""

    def __init__(self, age, sex=1, weight=0.0):
        self.age = age
        self.sex = sex
        self.weight = weight


a1 = Animal(2, 0, 10.0)
a2 = Animal(1, weight=5.0)
a3 = Animal(1, sex=0)

print('a1年龄：{0}'.format(a1.age))
print('a2体重：{0}'.format(a2.weight))
print('a3性别：{0}'.format('雌性' if a3.sex == 0 else '雌性'))
