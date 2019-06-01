#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Date: 2019/5/25


'''
下面说了一大堆，比较乱，用的时候，只需记住：
1.第一次send()时，只能是None或用next(),否则：TypeError: can't send non-None value to a just-started generator
2.n = yield r 中 n 最终所获的值是第二次send()的内容。
'''

def consumer():
    r = 'abc'
    while True:
        # n是由yield语句接收的send()的内容
        # 第一次send(None)或next()执行到下面这句(第一次yield)就停了，此时r='abc'，这里相当于只是启动。
        # 但却告诉了produce自己(consumer)是个生成器，此时，r='' ，下面的语句未执行。
        # 第二次send(),即下面的第一次调用send(n)后,即send(1)，执行下面的语句，此时，n=1,r='200 OK', n=1是由第一次yield接收的(虽然已经执行了，这个和函数调用类似)
        # 接着，第二次执行yield，接下来的就是一边生产，一边消费，不会存在冲突。
        # 一个需要注意的是，每次执行yield后，就跳转了，但跳转回来时yield会接收相应的n值，n对应send(n)中的n。
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    # 第一次调用时，请使用next()语句或是send(None)，不能使用send发送一个非None的值，否则会出错的，因为没有yield语句来接收这个值。
    # m = c.send(None)
    # 可以用一个m来接收看一下，此时m=abc,即接收的是第一次yield r 的值。
    m = next(c)
    print(m)
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
