#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Date: 2019/5/19

import pickle

d = dict(name='Bob', age=20, score=88)
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
print('序列化后的bytes为：', pickle.dumps(d))

# 或者使用pickle.dump()直接把对象序列化后写入一个file-like Object
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象。
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print('反序列化后的内容为：', d)
