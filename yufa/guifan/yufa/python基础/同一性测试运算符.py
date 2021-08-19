# coding=utf-8
# ！/usr/bin/env python3

from os import name


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __ed__(self, other):
        if __name__ == other.name and self.age == other.age:
            return True
        else:
            return False


p1 = Person('Tony', 25)
p2 = Person('Tony', 25)

print(p1 == p2)
print(p1 is p2)

print(p1 != p2)
print(p1 is not p2)
