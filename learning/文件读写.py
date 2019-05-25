#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Date: 2019/5/19

# 写
# f = open("file.txt", 'a', encoding='utf-8', errors='ignore')
# f.write("I try to write something new to file\n")
# f.close()

# 推荐用法
# with open("file.txt", 'a', encoding='utf-8', errors='ignore') as f:
#     for i in range(6):
#         f.write("I try to write something new to file\n")


# 读
f = open("file.txt", 'r', encoding='utf-8', errors='ignore')  # 默认以只读的形式打开
print(f.readline())  # 因为\n是写入的，所以打印出来时加上每一行的回车，即两个回车
print("当前指针位置", f.tell())  # tell 方法获取当前文件读取指针的位置
print(f.readline().strip())  # 可以用strip()将行末尾的换行符除去
print("当前指针位置", f.tell())
print(f.read())
print("读取当前指针位置", f.tell())
# seek 方法，用于移动文件读写指针到指定位置,有两个参数，第一个offset: 偏移量，需要向前或向后的字节数，正为向后，负为向前；
# 第二个whence: 可选值，默认为0，表示文件开头，1表示相对于当前的位置，2表示文件末尾
# 注意，关于偏移量，只有在以'b'(二进制)的条件下才可用，不然只可以为0。
f.seek(0, 0)
print("读取当前指针位置", f.tell())
f.seek(0, 2)
print("读取当前指针位置", f.tell())
f.seek(0)
print("读取当前指针位置", f.tell())
print(f.closed)
print(f.mode)
f.close()
print(f.closed)
# print(f.truncate(10))

print('**********************************分割线***********************************')

# 推荐用法
with open('file.txt', mode='r', encoding='utf-8', errors='ignore') as f:
    f = f.readlines()
    print(f)
    
    for each in f:
        print(each, end='  ')  # two space
