# coding=utf-8
# !/usr/bin/env python3

student_dict = {102:'张三',105:'李四',108:'王五'}

print('---遍历建----')
for student_id in student_dict.keys():
    print('学号:' + str(student_id))

print('---遍历建---')
for student_name in student_dict.values():
    print('学生:' + student_name)

print('---遍历建---')
for student_id,student_name in student_dict.items():
    print('学号： {0} - 学生：（1）'.format(student_id,student_name))