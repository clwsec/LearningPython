#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time: 2019/5/13

# 1、_xxx     不能用于’from module import *’ 以单下划线开头的表示的是保护变量，只能允许其本身与子类进行访问。
# 2、__xxx    双下划线的表示的是私有类型的变量(private)，只能是允许这个类本身进行访问了，连子类也不可以
# 3、__xxx__  定义的是特列方法，如__init__，__str__,__call__等
# 注：python中不存在protected的概念，上面所说的保护变量，应该把其看作私有变量使用，之所以称为保护变量是为了便于与private类型做区分。

class A(object):
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name


# 这个就是格式化后再当做参数传入对应属性
a = A('%s/%s' % ('dsad', 'abc'))

print(a.get_name())  # dsad/abc
# 下面的可以访问，不过根据python的约定，应该将其视作private，
# 不要在外部使用它们，良好的编程习惯是不要在外部使用它。
print(a._name)  # dsad/abc
