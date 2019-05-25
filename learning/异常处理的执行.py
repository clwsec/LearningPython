#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time: 2019/4/21

# 异常捕获
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


# 一般情况下使用的异常捕获
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


try:
    main()
except ZeroDivisionError as e:
    print(e)
else:
    print("当出现错误后，我便不再被执行")
finally:
    print("我是一定被执行的")
print('这里是程序打印完错误信息后的继续执行，并正常退出')
'''
# 抛出错误

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
'''
