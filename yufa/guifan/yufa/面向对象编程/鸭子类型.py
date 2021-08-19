# !/usr/bin/env python3
# coding:utf-8
import go


class Animal(object):
    def run(self):
        print('动物跑')


class Dog(Animal):
    def run(self):
        print('狗狗跑')


class Car:
    def run(self):
        print('汽车跑')


go(Animal())
go(Dog())
go(Car())
