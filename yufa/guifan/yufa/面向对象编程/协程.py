#! usr/bin/env python3
# coding=utf-8

def customer():#测试代码
    while True:
        number = yield
        print('开始消费：', number)


custom = customer()
next(custom)
for i in range(5):
    print('开始生产：', i)
    custom.send(i)
