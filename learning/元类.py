#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Date: 2019/5/18

# 将类的属性都应该是大写形式，首先用简单的方法写
# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    
    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)


# __metaclass__ = upper_attr # 这会作用到这个模块中的所有类，这是Python2的用法，如果__metaclass__ = upper_attr写在类中，就只会作用于对应的类中
# Python3用法如下。
class Foo(object, metaclass=upper_attr):  # 这里好像也是个细节，Python2中不可以有object
    # 只会作用于这个类中
    # __metaclass__ = upper_attr # Python2若是这样写，就只会作用于次类中，效果和当前Python3中的效果一样。
    bar = 'bip'


print(hasattr(Foo, 'bar'))
# 输出: False
print(hasattr(Foo, 'BAR'))
# 输出:True

f = Foo()
print(f.BAR)
# 输出:'bip'


print("*********************************分割线************************************")


# 用一个真正的class来当做元类。
# 请记住，'type'实际上是一个类，就像'str'和'int'一样，所以，你可以从type继承
class UpperAttrMetaclass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        # 复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        return type.__new__(upperattr_metaclass, future_class_name, future_class_parents, uppercase_attr)


'''
# 或将参数改短一点
class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr  = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(cls, name, bases, uppercase_attr)

# 如果使用super方法的话，我们还可以使它变得更清晰一些，这会缓解继承（是的，你可以拥有元类，从元类继承，从type继承）
class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)
'''


class Foo1(object, metaclass=UpperAttrMetaclass):  # 这里好像也是个细节，Python2中不可以有object
    # 只会作用于这个类中
    # __metaclass__ = upper_attr # Python2若是这样写，就只会作用于次类中，效果和当前Python3中的效果一样。
    bar = 'bip'


print(hasattr(Foo1, 'bar'))
# 输出: False
print(hasattr(Foo1, 'BAR'))
# 输出:True

f = Foo1()
print(f.BAR)
# 输出:'bip'
