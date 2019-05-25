#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time: 2019/5/2

# 可写为生成器的函数中使用yield即为生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# generator函数的“调用”实际返回一个generator对象
print(fib(6))

# 通过for循环访问
for i in fib(6):
    print(i)

# 通过捕获StopIteration错误，获取return返回值，返回值包含在StopIteration的value中，用return无用。
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# 杨辉三角生成器实现
def triangles(n):  # n 为需要生成的行数加1
    p = [1]
    while True:
        yield p  # generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
        p = [1] + [p[i] + p[i + 1] for i in range(len(p) - 1)] + [1]
        if len(p) == n:
            break


n = 11
for t in triangles(n):
    print(t)
