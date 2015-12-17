# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 23:06:01 2015

@author: zouqi
"""

"""
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
练习要点：
    1.range 的使用
    2.and 是 且的意思
    3.itertools库的使用
    4.使用list接收一个Object
"""
import itertools


def exampl1():
    """
    输出123至432之间三位数不重复的组合
    """
    for i in range(123, 432):
        hundreds = i / 100
        decade = i / 10 - hundreds * 10
        uint = i - decade * 10
        if hundreds != decade and hundreds != uint and decade != uint:
            print i


def exampl2():
    """
    符合题目要求，使用itertools库
    """
    print list(itertools.permutations([1, 2, 3, 4], 3))


if __name__ == '__main__':
    # exampl1()
    exampl2()
