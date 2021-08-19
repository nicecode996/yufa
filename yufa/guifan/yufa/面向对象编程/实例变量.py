# coding=utf-8
# ！/usr/bin/env python3

class Animal(object):
    """定义动物类"""

    def __init__(self, age, sex, weight):              # 构造方法创建和初始化实例变量
        self.age = age                                 # 创建和初始化实例变量
        self.sex = sex
        self.weight = weight


animal = Animal(2, 1, 100.0)

print('年龄:{0}'.format(animal.age))
print('性别:{0}'.format('雌性' if animal.sex == 0 else '雄性'))
print('体重:{0}'.format(animal.weight))
