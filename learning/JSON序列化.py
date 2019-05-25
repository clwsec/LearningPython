#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Date: 2019/5/19

import json

d = dict(name='Bob', age=20, score=88)
# dumps()方法返回一个str，内容就是标准的JSON。
print('序列化后的bytes为：', json.dumps(d))

# 类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 注意，这里是以'w'的形式写，因为dump()方法返回的是str
f = open('dumps.txt', 'w')
json.dump(d, f)
f.close()

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
f = open('dumps.txt', 'r')
d = json.load(f)
f.close()
print('反序列化后的内容为：', d)

print('*********************************************************')
# 看看dumps()参数
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
# 默认为True
ss = json.dumps(obj)
print(ss)

sss = json.dumps(obj, ensure_ascii=False)
print(sss)

print(json.loads(s))
print(json.loads(ss))
print(json.loads(sss))

print('*********************************************************')
# JSON进阶
import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)


# print(json.dumps(s))
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，
# 只需要为Student专门写一个转换函数，再把函数传进去即可：
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


# 如果要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


# 这样即可序列化对象
print(json.dumps(s, default=student2dict))

# 或者直接这样，因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
# 也有少数例外，比如定义了__slots__的class。
print(json.dumps(s, default=lambda obj: obj.__dict__))
print(s.__dict__)

# 在反序列化时必须要有相应的方法
json_str = json.dumps(s, default=student2dict)
json_str1 = json.dumps(s, default=lambda obj: obj.__dict__)
print(json.loads(json_str, object_hook=dict2student))
print(json.loads(json_str1, object_hook=dict2student))
