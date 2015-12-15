# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.15 23:15 

"""

"""
    生成器 <==>Generator
    用于解决生成大量的数据，用算法节约空间。
"""


def run():
    generator = (x * x for x in range(0, 10))  # 生成器的表达式范型
    for i in range(5):
        print generator.next()

    # 使用yield制作一个生成器
    # yield的原理
    def odd():
        print 'step 1'
        yield 1
        print 'step 2'
        yield 3
        print 'step 3'
        yield 5

    # 一种错误的写法
    """
    当一个函数作为生成器时，要将其转换为一个实体对象。
    这样它才有存储空间，进行想要的操作不是
    """
    print odd().next()
    print odd().next()
    print odd().next()
    # 正确的写法
    o = odd()
    print o.next()
    print o.next()
    print o.next()
    print("hello")

    # 制作一个数列的生成器-切波列数列
    def fib(max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            a, b = b, a + b
            n = n + 1

    for n in fib(10):
        print n, ' ',

    print fib(10)

    # 制作一个数列生成器-等差数列
    def grade(max):
        diff = 10
        n, i = 0,0
        while i < max:
            yield n
            n += diff
            i = i + 1

    for n1 in grade(10):
        print n1, ' ',


if __name__ == "__main__":
    run()
