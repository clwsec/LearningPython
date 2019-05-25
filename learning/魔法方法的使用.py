#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time: 2019/5/13

'''
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print(Chain('%s/%s' % (self._path, path)))
        return Chain('%s/%s' % (self._path, path)) # 把一个对象当成函数调用，会自动调用__str__方法，不止，因为还调用了__init__方法

    def __str__(self):
        return self._path

    __repr__ = __str__

a = Chain().status.user.timeline.list
print(a)

# print(Chain().users('michael').repos)

'''


# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self):
#         print('My name is %s.' % self.name)
#         return '调用了__call__'
#
#     def __str__(self):
#         return self.name
#
# s = Student('Michael')
# # 显式把对象用成函数则调用__call__
# print(s())
#
# print('-------------------------------------------------------')
#
# # 把对象当字符串使用则调用__str__
# print(Student('Michael'))

class Chain(object):
    
    def __init__(self, path=''):
        print('调用了__init__方法：')
        self._path = path
    
    def __getattr__(self, path):
        # print('调用了__getattr__方法：')
        print('调用了__getattr__方法：', Chain('%s/%s' % (self._path, path)))
        return Chain('%s/%s' % (self._path, path))  # 把一个对象当成函数调用，会自动调用__str__方法，不止，因为还调用了__init__方法
    
    def __str__(self):
        print('调用了__str__方法：')
        return self._path
    
    def __call__(self, path):
        print('调用了__call__方法：', Chain('%s/%s' % (self._path, path)))
        return Chain('%s/%s' % (self._path, path))
    
    __repr__ = __str__


# tem = Chain()
# tem = tem.users('Bob')

print(Chain().users('michael').repos)  # /users/michael/repos

'''
class urls(Chain):
    def __init__(self, path='/users'):
       self.__path = path

   def __getattr__(self, path):
       return urls(('%s/%s' % (self.__path, path)))

    def __call__(self, path):
       return urls(('%s/%s' % (self.__path, path)))

   def __str__(self):
       return self.__path

   __repr__ = __str__

'''
