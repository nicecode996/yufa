# ！/usr/bin/env python3
# coding=utf-8

import sys

score = int (sys.argv[1])

result = '及格' if score >= 60 else '不及格'

print(result)