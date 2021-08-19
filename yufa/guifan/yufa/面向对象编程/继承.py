# coding=utf-8
# !/usr/bin/env python3

class ParentClass1:
    def run(self):
        print('ParentClass1 run...')


class ParentClass2:
    def run(self):
        print('ParentClass2 run...')


class SubClass1(ParentClass1, ParentClass2):
    pass


class Subclass2(ParentClass2, ParentClass1):
    pass


class Subclass3(ParentClass1, ParentClass2):
    def run(self):
        print('SubClass3 run...')


sub1 = SubClass1()
sub1.run()
sub2 = Subclass2()
sub2.run()
sub3 = Subclass3()
sub3.run()
