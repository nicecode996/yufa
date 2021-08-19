# coding=utf-8
# !/usr/bin/env python3

def print_area(wight, height):
    area = wight * height
    print("{0} * {1} 长方形的面积：{2}".format(wight, height, area))


print_area(320.0, 480.0)                 # 没有采用关键字参数函数调用
print_area(wight=320.0, height=480.0)    # 采用关键字参数函数调用
print_area(320.0, height=480.0)          # 蚕蛹关键字参数函数调用
# print_area(width=320.0,height)         # 发生错误
print_area(height=480.0, wight=320.0)    # 采用关键字参数函数调用
