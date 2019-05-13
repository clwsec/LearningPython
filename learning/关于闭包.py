#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time:2019/4/21

# 关于闭包
def outer():
    x = 1
    y = 'a'

    def inner():
        print(x, y)  # 1

    return inner


foo = outer()
print(foo.__closure__)  # 2
foo()

# 这里内容无关，只是看看相应的用法
print("-------------------分割线-----------------------")
print(foo.__name__)
print(foo.__class__)
print(foo.__annotations__)
print(foo.__dir__())

# https://yunjianfei.iteye.com/blog/2186092
# 闭包的理解
# python里运行的东西，都按照作用域规则来运行。
# 1. x是outer函数里的local变量
# 2. 在#1处，inner打印x,y时，python在inner的locals中寻找x，找不到后再到外层作用域（即outer函数）中寻找，找到后打印。
#
# 看起来一切OK，那么从变量生命周期（lifetime）的角度看，会发生什么呢：
# 1. x,y是outer的local变量，这意味着只有outer运行时，x,y才存在。那么按照python运行的模式，我们不能在outer结束后再去调用inner。
# 2. 在我们调用inner的时候，x,y应该已经不存在了。应该发生一个运行时错误或者其他错误。但是这一些都没有发生，inner函数依旧正常执行，打印了x,y。
#
# 解释
# Python支持一种特性叫做函数闭包（function closures）：在非全局（global）作用域中定义inner函数（即嵌套函数）时，会记录下它的嵌套函数namespaces（嵌套函数作用域的locals）
# 可以称作：定义时状态，可以通过__closure__ 这个属性来获得inner函数的外层嵌套函数的namespaces。(如上例中#2，打印了foo.__closure__，里面保存了一个int对象和一个str对象，分别对应x和y)
#
# 注意：每次调用outer函数时，inner函数都是新定义的。上面的例子中，x,y是固定的，所以每次调用inner函数的结果都一样。
#
# 所以，闭包实际上是记录了外层嵌套函数作用域中的local变量。


# # 再看闭包思考
# # 闭包的使用，注意内层函数返回的是函数名
# def createCounter():
#     # 注意，l = [0]只会在调用createCounter()时调用，这里使用列表，是因为其是可变变量，如果是数值型，则会出错。
#     l = [0]
#     def counter():
#         l[0] += 1
#         return l[0]
#     # 返回函数名,可看作函数的引用
#     return counter


# # 若是这样，则出错：UnboundLocalError: local variable 'i' referenced before assignment
# # 因为：在当前作用域中的给变量赋值时，该变量将成为该作用域的局部变量，并在外部范围中隐藏任何类似命名的变量。
# # 而上面的情况就不会，因为可变变量l所指向的对象始终没有变（只是其内容变了）
# # 这类似元组本身是不可变的，但是元组内的列表元素的内容是可变的
# def createCounter():
#     i = 0
#     def counter():
#         i = 1 + i
#         return i
#     return counter
#
# 测试:
# counterA = createCounter()
# # print(type(counterA))
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')
