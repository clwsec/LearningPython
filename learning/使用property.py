#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time: 2019/5/13


# 若定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
class Student(object):
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
    
    @property
    def name(self):
        return self._name


s = Student()
s.score = 60  # OK，实际转化为s.set_score(60)
print(s.score)  # OK，实际转化为s.get_score()


# s.score = 999 # 出错: score must between 0 ~ 100!
# s.name = 'Bob' # 出错: can't set attribute


# 这个例子说明方法名不应该和属性名重合，否则会报错：RecursionError: maximum recursion depth exceeded
# 在实际应用中应该像上面的写法，方法名和属性名应该有区别。当然，下面的测试发现也没错。
class Screen(object):
    
    @property
    def width1(self):
        print(self.width)
    
    @width1.setter
    def width1(self, w):
        self.width = w
    
    @property
    def height1(self):
        print(self.height)
    
    @height1.setter
    def height1(self, h):
        self.height = h
    
    @property
    def resolution(self):
        return self.width * self.height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
