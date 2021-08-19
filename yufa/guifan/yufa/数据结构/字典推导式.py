# coding=utf-8
# !/usr/bin/env python3

input_dict = {'one':1,'two':2,'three':3,'four':4}

output_dict = {k:v for k ,v in input_dict.items() if v % 2 == 0}
print(output_dict)

keys = {k for k, v in input_dict.items() if v % 2 == 0}
print(keys)