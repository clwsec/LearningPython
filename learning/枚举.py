#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Date: 2019/5/18

# http://python.jobbole.com/84112/
from enum import Enum, IntEnum, unique

'''
enum 提供了 Enum/IntEnum/unique 三个工具，可以通过继承 Enum/IntEnum 定义枚举类型。
其中，IntEnum 限定枚举成员必须为（或可以转化为）整数类型，而 unique 方法可以作为修饰器限定枚举成员的值不可重复。
'''
# 例子1：
try:
    @unique
    class WEEKDAY(Enum):
        MON = 1
        TUS = 2
        WEN = 3
        THU = 4
        FRI = 1
except ValueError as e:
    print(e)  # 出错duplicate values found in <enum 'WEEKDAY'>: FRI -> MON
print('********************************分割线*****************************************')


# 例子2
class Color(Enum):
    R = 0
    G = 1
    B = 2


# 可以赋值给变量，但不可不可实例化，如Color.R = 3就是错的
red = Color(0)
green = Color(1)
blue = Color(2)

print(red, green, blue)

# 可以进行比较判断
print(red is Color.R)
print(red == Color.R)
print(red is blue)
print(green != Color.B)
print(red == 0)  # 不等于任何非本枚举类的值

# 由于枚举成员本身也是枚举类型，因此也可以通过枚举成员找到其它成员
print(red.B)
print(red.B.G.R)

# 通过属性访问
print(red.name, ':', red.value)

# 遍历访问
for color in Color:
    print(color.name, '=>', color.value)

# 如果要遍历Enum中带有重复的枚举成员，可能会用到__members__方法,注意，这里没有重复的
for name, member in Color.__members__.items():
    print(name, '=>', member, ',', member.value)
