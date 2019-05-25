#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Date: 2019/5/19

# 注释中的代码可执行，通过doctest模块
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x # 把下面100去掉，会提示Expected nothing
    100
    >>> d1.y = 200
    >>> d1['y'] # 可以吧y改成z看看效果，会出错KeyError。
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)
    
    # 也可以通过注释某个方法，看看是何情况
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    
    def __setattr__(self, key, value):
        self[key] = value


# 当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest。
if __name__ == '__main__':
    import doctest
    
    doctest.testmod()

# # 作业
# def fact(n):
#     '''
#     Calculate 1*2*...*n
#
#     >>> fact(1)
#     1
#     >>> fact(10) # 不用自己算，运行时出错会有结果，到时再改即可
#     3628800
#     >>> fact(-1) # doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间一大段烦人的输出。
#     Traceback (most recent call last):
#       ...
#     ValueError
#     '''
#     if n < 1:
#         raise ValueError()
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
