#coding=utf_8
#推荐

import re
import struct
import binascii

#不推荐

import re, struct,binascii

#可以 from import 后面跟多个代码元素是可以的

from codeop import  CommandCompiler, compile_command

# 导入语句按照从通用到特殊的顺序分组，顺序是：标准库—>第三方库->自己模块。每
#一组之间有一个空行，而且组中模块是按照英文字母顺序排序的。

import io   #导入标准库中的代码
import os
import  pkgutil
import re
import sys
import time

from html import unescape  #导入第三方库中的模块

#from com.pkg1 import example   此处包名不应加注释，应没有此包，故加注释防止系统报错
