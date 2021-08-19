# coding=utf-8
# !/usr/bin/env python3

class Animal(object):
    def __init__(self, age, sex, weight=0.0):
        self.age = age
        self.sex = sex
        self.__weight = weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight
        a1 = Animal(2, 0, 10.0)
        print('a1体重: {0:0.2f}'.format(a1.get_weight()))
        a1.set_weight(123.45)
        print('a1 体重: {0:0.2f}'.format(a1.get_weight()))
