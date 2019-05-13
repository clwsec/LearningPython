#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time: 2019/4/21
a = 1
try:
    a += 1
except:
    a += 1
else:  # 这里也会执行
    a += 1
finally:
    a += 1
print(a)
