#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Date: 2019/5/25

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    # 第一次调用时，请使用next()语句或是send(None)，不能使用send发送一个非None的值，否则会出错的，因为没有yield语句来接收这个值。
    # c.send(None)
    next(c)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        # s接收的是consumer中yield的r
        s = c.send(n)
        print('[PRODUCER] Consumer return: %s' % s)
    c.close()


c = consumer()
produce(c)

'''
注意到consumer函数是一个generator，把一个consumer传入produce后：

1.首先调用c.send(None)启动生成器；
2.然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
3.consumer通过yield拿到消息，处理，又通过yield把结果传回；
4.produce拿到consumer处理的结果，继续生产下一条消息；
5.produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

关于yield和send的区别：http://www.cnblogs.com/coderzh/articles/1202040.html
'''
