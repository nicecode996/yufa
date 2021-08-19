# coding=utf-8

a = 1
b = 2

a += b
print("a | b = {0}".format(a))

a += b + 3
print("a + b + 3 = {0}".format(a))

a -= b
print("a - b = {0}".format(a))

a *= b
print("a * b = {0}".format(a))

a /= b
print("a / b = {0}".format(a))

a %= b
print("a % b = {0}".format(a))
print("--------------------------")
a = 0b10110010
b = 0b01011110

a |= b
print("a | b = {0}".format(a))

a ^= b
print("a ^ b = {0}".format(a ^ b))
