#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time: 2019/4/21

# https://www.zhihu.com/question/26930016/answer/99243411
# 简单的装饰

# def 炼丹炉(func): # func就是‘孙悟空’这个函数
#   def 变身(*args, **kwargs): #*args, **kwargs就是‘孙悟空’的参数列表，这里的‘孙悟空’函数没有传参数，我们写上也不影响，建议都写上
#       print('有火眼金睛了') # 加特效，增加新功能，比如孙悟空的进了炼丹炉后，有了火眼金睛技能
#       return func(*args, **kwargs) #保留原来的功能，原来孙悟空的技能，如吃桃子
#   return 变身 # 炼丹成功，更强大的，有了火眼金睛技能的孙悟空出世
#
# @炼丹炉
# def 孙悟空():
#   print('吃桃子')
#
# 孙悟空()


# 扩展权限认证

# # userAge = 9
# userAge = 30
#
# def canYou(func):
#   def decorator(*args, **kwargs):
#       if userAge > 1 and userAge < 10:
#           return func(*args, **kwargs)
#       print('你的年龄不符合要求，不能看')
#   return decorator
#
# @canYou
# def play():
#   print('开始播放动画片 《喜洋洋和灰太狼》')
#
# play()


# 使用多个装饰器
# 下面这个链接讲的不错，但是应该还有一个问题没有解决，即：多个装饰器使用时内部的装饰是嵌套调用
# 的，那同样的return func(*args, **kwargs)岂不是有多次执行，所以在实现时，应该还有删减（使f只调用一次）。
# https://segmentfault.com/a/1190000007837364

# 其实，在实际使用中不必考虑这么多，按正常理解，从上到下装饰即可，下面这个例子很贴切

# def 炼丹炉(func):
#   def 变身(*args, **kwargs):
#       print('有火眼金睛了')
#       return func(*args, **kwargs)
#   return 变身
#
# def 龙宫走一趟(func):
#   def 你好(*args, **kwargs):
#       print('有金箍棒了')
#       return func(*args, **kwargs)
#   return 你好
#
# def 拜师学艺(func):
#   def 师傅(*args, **kwargs):
#       print('学会飞、72变了')
#       return func(*args, **kwargs)
#   return 师傅
#
# @拜师学艺
# @龙宫走一趟
# @炼丹炉
# def 孙悟空():
#   print('吃桃子')
#
# 孙悟空()

# 上面代码的等效于 拜师学艺(龙宫走一趟(炼丹炉(孙悟空)))
# 代码的执行顺序是 从内到外
# 先执行 炼丹炉，然后是龙宫走一趟，最后是拜师学艺，但打印出的却是相反的（和按代码从上到下的顺序执行一样）原理参考上面那个链接


# 作业，写一个装饰器
# import time
# from functools import wraps
#
# def metric(func):
#     @wraps(func)
#     def printTime(*args, **kwargs):
#         print('begin call')
#         t1 = time.time()
#         result = func(*args, **kwargs)
#         t2 = time.time()
#         print('%s executed in %.4f ms' % (func.__name__, t2 - t1))
#         print('end call')
#         return result
#     return printTime
#
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
# else:
#     print('测试成功')


# 思考，如何使@log既可有参数，也可无参数，其他方法未知。
import functools


def log(txt=None):
    def decorator(func):
        # 下面这行注释掉，则print(now.__name__)打印出wrapper
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (txt, func.__name__))
            return func(*args, **kw)
        
        return wrapper
    
    return decorator


@log('excute')
def now():
    print('2015-3-25')


now()
# print(now.__name__)
