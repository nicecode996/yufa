# conding=utf_8
# import 语句前后保留两个空行

# 函数声明之前保留两个空行 示例代码如下：
'''
from _weakrefest import WeakSet


def abc(d):

'''


# 类声明之前保留两个空行，示例代码如下：
from datetime import datetime


class abc(classmethod):
    __isabstractmethod__ = True

    def __init__(self, callable):
        callable._isabstractmethod_ = True
        super().__init__(callable)


# 方法之前声明保留一个空行，示例代码如下
class abc(classmethod):
    __isabstractmethod__ = True

    def __init__(self):
        callable._isabstractmethod_ = True
        super().__init__(callable)

    # 两个逻辑代码块之间应该保留一个空行，示例代码如下，其中1处是空行。
    def convert_timestmap(val):
        datepart, timepart = val.split(b" ")
        year, mouth, day =map(int,datepart.split(b" "))
        timepart_full = timepart.split(b".")
        hours, minutes, seconds = map(int, timepart_full[0].split(b":"))
        if len(timepart_full) == 2:
            microseconds = int('{:0<6.6}'.format(timepart_full[1].decode()))
        else:
            microseconds = 0
        #此处为1 为空行
        val = datetime.datetime(year, mouth, day, hours, minutes, seconds, microseconds)
        return val