# conding=utf-8
# ! /usr/bin/env python
'''
list_square = []
for i in range(10):
    if i % 9 == 0:
        list_square.append(i ** 2)
        print(i)
# print(list_square)

# 0~9中偶数的平方数列也可以通过列表推导式实现，代码如下：
list_square = [x ** 2 for x in range(10) if x % 2 == 0]
print(list_square)
'''

list_square4 = [i * j for i in range(1, 4) for j in range(1,4)]
# for j in range(1, 4)]
# for i in range(1, 4):
#     for j in range(1, 4):
#         list_square4.append(i * j)
print(list_square4)
