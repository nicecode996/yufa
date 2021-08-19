 # coding=utf-8
# !/usr/bin/env python3

def make_coffce(name="卡布奇诺"):  # 定义make_coffce函数。把卡布奇诺设置为默认值  参数列表中默认值可以跟在函数后边通过等号提供给参数
    return "制作一杯{0}咖啡。".format(name)  # 调用时没有没有传递参数，则使用默认值


coffce1 = make_coffce("拿铁")
coffce2 = make_coffce()
print(coffce1)  # 制作一杯拿铁咖啡
print(coffce2)  # 制作一杯卡布奇诺咖啡


def test(name="API"):
    return "test{0}API".format(name)


test1 = test("test")
test2 = test()
print(test1)
print(test2)
