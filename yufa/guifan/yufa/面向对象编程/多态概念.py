# !/usr/bin/env python3
# coding:utf-8

# 几何图形
class Figure:
    def draw(self):
        print('绘制Figure...')


# 椭圆形
class Ellipse(Figure):
    def draw(self):
        print('绘制Ellipse...')


# 三角形
class Triangle(Figure):
    def draw(self):
        print('绘制Triangle...')


f1 = Figure()
f1.draw()

f2 = Ellipse()
f2.draw()

f3 = Triangle()
f3.draw()
