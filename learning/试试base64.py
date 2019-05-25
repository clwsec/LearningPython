#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Date: 2019/5/23

import base64
import collections
import requests
import itertools


def safe_base64_decode(s):
    while len(s) % 4 > 0:
        s += b'='
    return base64.b64decode(s)


# 测试:
# 这个assert后面似乎不起作用啊
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

# 查看模块内容，其实在IDE中直接看源码更快
print(collections.__doc__)
print(collections.__all__)
# print(itertools.__doc__)
print(dir(itertools))
print('查看可供调用的接口信息：', base64.__all__)
print('第三方模块位置：', requests.__file__)
print('内置模块位置：', collections.__file__)
print('查看模块定义了哪些变量、函数和类：', dir(requests))
