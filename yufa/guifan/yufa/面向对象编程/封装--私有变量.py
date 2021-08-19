# coding=utf-8
# !/usr/bin/env python3

class Animal(object):
    """定义动物类"""

    def __init__(self, age, sex=1, weight=0.0):
        self.age = age
        self.sex = sex
        self.__weight = weight

    def eat(self):
        self.__weight += 0.5
        print('eat...')

    def run(self):
        self.__weight -= 0.01
        print('run...')


a1 = Animal(2, 0, 10.0)

print('a1体重:{0:0.2f}'.format(a1._Animal__weight))
a1.eat()
a1.run()
