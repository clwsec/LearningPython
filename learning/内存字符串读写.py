#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Date: 2019/5/19

from io import StringIO
from io import BytesIO

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
f = StringIO()
f.write('Hello World')
s = f.readline()
print(s)  # 这里读不出来，是因为文件读写指针已经到文件末尾了，可用getvalue()来读
print(f.getvalue())
# 或者先设置文件指针位置
f.seek(0)
s = f.readline()
print(s)
f = StringIO('abc')
print(f.read())
print("*****************************分割线******************************")

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
f = BytesIO(b'abc')
print(f.read())
