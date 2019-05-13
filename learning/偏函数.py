#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time: 2019/5/11

from functools import partial

# 转为二进制
int2 = partial(int, base=2)
print(int2('1010'))

# 因为上面是默认参数，所以这里依然可以设置关键字参数base的值
print(int2('1010', base=10))

max2 = partial(max, 10)
# 会把10作为*args的一部分自动加到左边
max2(5, 6, 7)
# 相当于
args = (10, 5, 6, 7)
print(max(*args))
