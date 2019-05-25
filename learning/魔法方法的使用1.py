#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Date: 2019/5/19

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b
    
    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值
    
    def __getitem__(self, n):
        # 使用下标访问
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        # 实现简单的切片
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


for n in Fib():
    print(n, end=' ')
print()

f = Fib()
print("使用切片功能：", f[:6])
print("使用下标访问:", f[0], f[1], f[2], f[3], f[4], f[5])
