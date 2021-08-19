# coding=utf-8
# ！/usr/bin/env python3

n_list = { x for  x in range(100) if x % 2 == 0 if x % 5 == 0 }
print(n_list)


print('--------------------')

input_list = [2,3,2,4,5,6,6,6]
print(n_list)

n_set = {x ** 2 for x in input_list}
print(n_set)