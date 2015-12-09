# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.09 22:54 

"""
"""
题目：求一个3*3矩阵对角线元素之和。
    1.二维数组
        1.1.python是如何实现多维数组的
            以list为例，相当于一个List里面又保存了一个list其索引的方式，就是
            C语言熟悉的二维数组的方式
        1.2.python二维数组与C语言数组的区别
            形如：b = [1, 2, 3, 4, ['a', 2, 3, 4, 5]]
            当你访问b[0][0]的时候，程序会提示你报错
            但当你访问b[4][0]时，程序可以成功访问。
            Python创建数组的灵活性，降低了其访问数组的效率。
        1.3.多维数组避免浅拷贝的问题
            参见1.3的代码
            当你修改一个元素时，其他元素的数值也跟着产生了变化
            1.3.1 浅拷贝与深拷贝的关系
                在python中，当你给一个对象赋值时，实际上，只是
                让该对象指向了被赋值的对象，可理解为
                    a=b
                    a指向了b
                    当b产生改动时，a自然跟着发生变动，这就是浅拷贝
                参考链接：http://www.01happy.com/python-shallow-copy-and-deep-copy/


"""
import random


def run():
    # 1.3创建一个二维矩阵
    c = [[0] * 3] * 4
    print c
    c[0][0] = 1
    print c
    print u'对象的ID:',id(c[0][0]),id(c[1][0])
    # 随机产生一个二维矩阵
    a = [[random.randint(0, 9) for i in range(3)] for i in range(3)]  # 随机生成一个二维矩阵
    print a
    print u'对象的ID:',id(a[0][0]),id(a[1][0])
    a[0][0] = 1
    print a[0][0]
    print a

    b = [1, 2, 3, 4, ['a', 2, 3, 4, 5]]
    print b[4][0]
    print("hello")


if __name__ == "__main__":
    run()
