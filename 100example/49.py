# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.12 08:34 

"""
"""
题目：使用lambda来创建匿名函数。
    1. 使用Python写一些执行脚本时，使用lambda可以省去定义函数的过程，让代码更加精简。
    2. 对于一些抽象的，不会别的地方再复用的函数，有时候给函数起个名字也是个难题，使用lambda不需要考虑命名的问题。
    3. 使用lambda在某些时候让代码更容易理解。
    4. 像if或for或print这种语句就不能用于lambda中，lambda一般只用来定义简单的函数。
"""


def run():
    a = 20
    b = 30
    g = lambda x, y: x * y
    print g(a, b)


if __name__ == "__main__":
    run()
