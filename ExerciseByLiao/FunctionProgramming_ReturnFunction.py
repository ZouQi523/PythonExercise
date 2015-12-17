# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.16 16:25

"""

"""
    ReturnFunction <==> 返回函数
    这种返回一个函数的形式，由称为闭包。
"""

import random


def run(*args):
    d = 100

    def sum_num():
        n = 0
        for i in args:
            n += i
        return n

    return sum_num


# 一个闭包的简单应用
def player(name=''):
    jan_ken_list = {1: '剪刀', 2: '石头', 3: '布'}

    def Hand():
        string = name
        string += '出'
        string += jan_ken_list[random.randint(1, 3)]
        return string

    return Hand

if __name__ == '__main__':
    a = run(1, 2, 3, 4, 5, 6, 7)
    b = run(2, 3, 4, 5, 6, 7, 8)
    print 'a\'s address:', a
    print a(), ' ', b()
    playa = player('小明')
    playb = player('小强')
    playc = player('zouqi')
    print playa(), playb(), playc()
