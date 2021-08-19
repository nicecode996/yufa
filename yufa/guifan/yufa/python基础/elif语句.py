# coding=utf_8
# ！/usr/bin/env python3

import sys

score = int(sys.argv[1])

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = '不及格'

print("Grade = " + grade)