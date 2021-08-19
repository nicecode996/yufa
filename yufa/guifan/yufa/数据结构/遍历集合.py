# coding=utf-8
# !/usr/bin/env/python3

studtent_set = ('张三', '李四', '王五')

for item in studtent_set:
    print(item)

print('-----------------------')
for i, item in enumerate(studtent_set):
    print('{0} - {1}'.format(i, item))
