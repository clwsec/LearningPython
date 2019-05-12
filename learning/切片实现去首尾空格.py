#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time: 2019/5/2

# 看到的很简洁的写法
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


if __name__ == '__main__':
    # 测试:
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')
