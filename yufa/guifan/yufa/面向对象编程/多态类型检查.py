# !/usr/bin/env python3
# coding:utf-8

# 几何图形
class Figure:
    def draw(self):
        print('绘制Figure...')


class Ellipse(Figure):
    def draw(self):
        print('绘制Ellipse')


class Triangle(Figure):
    def draw(self):
        print('绘制Triangle')


f1 = Figure()
f1.draw()

f2 = Ellipse()
f2.draw()

f3 = Triangle()
f3.draw()

print(isinstance(f1, Triangle))
print(isinstance(f2, Triangle))
print(isinstance(f3, Triangle))
print(isinstance(f2, Figure))
