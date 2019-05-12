#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time: 2019/4/30

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        # 整体的思路就三步，细节通过递归取完成，三个盘以上脑算真的有点困难
        # 其实只需用三个盘心算结果和函数结果对比，一样即可知算法正确
        move(n - 1, a, c, b)  # 将上面n-1个盘移到b柱
        move(1, a, b, c)  # 将最下面的盘移到c柱
        move(n - 1, b, a, c)  # 将b柱上的n-1个盘移到c柱


move(3, 'a', 'b', 'c')
