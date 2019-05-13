#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time: 2019/5/2

def findMinAndMax(s):
    MAX = None
    MIN = None
    if len(s) == 0:
        return (MIN, MAX)
    else:
        a = s[0]
        b = s[0]
        for i in s:
            if i > b:
                b = i
            if i < a:
                a = i
        MIN = a
        MAX = b
        return (MIN, MAX)


if __name__ == "__main__":
    # 测试
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')
