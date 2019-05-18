#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time: 2019/4/21
# a = 1
# try:
#     a += 1
# except:
#     a += 1
# else:  # 这里也会执行
#     a += 1
# finally:
#     a += 1
# print(a)


try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
