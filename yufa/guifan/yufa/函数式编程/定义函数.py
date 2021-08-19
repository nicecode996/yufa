# coding-utf-8
# !/usr/bin/env python3

def rectangle_area(wight, height):
    area = wight * height
    return area


r_area = rectangle_area(320.0, 480.0)

print("320*480的长方形的面积：{0:.2f}".format(r_area))