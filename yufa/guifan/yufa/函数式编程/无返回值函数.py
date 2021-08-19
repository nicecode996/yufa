# coding=utf-8
# !/usr/bin/env python3

def show_info(sep=':',**info):
    """定义""可变参数函数"""
    print('------info--------')
    for key,value in info.items():
        print('{0} {2} {1}'.format(key,value,sep))
    return

result = show_info('->',name='Tony',age=18,sex=True)
print(result)

def sum(*numbers,multiple=1):
    """定义""可变参数函数"""
    if len(numbers) == 0:
        return
    total = 0.0
    for numbers in numbers:
        total += numbers
        return total * multiple
print(sum(30.0,80.0))
print(sum(multiple=2))