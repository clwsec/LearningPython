#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time: 2019/5/4

# # 这里，规范用户名输入
# def normalize(name):
#     return name[:1].upper() + name[1:].lower()
#
# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
#
# # map返回的是map对象地址
# L3 = map(normalize, L1)
# print(L3)
#
#
# # Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# from functools import reduce
# def prod(L):
#     return reduce(lambda x, y: x * y, L)
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')
#
#
# # 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# def str2float(s):
#     # print(list(map(lambda x: float(x) / 1000, s.replace('.', ''))))
#     return reduce(lambda x, y: x * 10 + y, list(map(lambda x: float(x) / 1000, s.replace('.', ''))))
#
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
