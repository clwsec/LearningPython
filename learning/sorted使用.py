#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time: 2019/5/10

# 按名字排序
def by_name(t):
    return t[0]


# 按成绩排序
def by_score(t):
    # return t[1]
    # 升级
    return -t[1]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)

# L2 = sorted(L, key=by_score, reverse=True)
L2 = sorted(L, key=by_score)
print(L2)
