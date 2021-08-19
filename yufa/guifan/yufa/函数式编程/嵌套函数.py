# coding-utf-8
# !/usr/bin/env python3

def calculate(n1,n2,opr):
    multiole = 2

    # 定义相加函数
    def add(a,b):
        return (a + b) * multiole

    # 定义相减函数
    def sub(a,b):
        return (a - b) * multiole

    if opr == '+':
        return add(n1,n2)
    else:
        return sub(n1,n2)

print(calculate(10,5,'+'))