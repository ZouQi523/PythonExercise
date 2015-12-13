# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.13 22:33 

"""
"""
    列表生成式 <==> the list of emergent
    用于简单的形式生成需要使用的列表
    列表生成器的优势在于用更简约的代码做一件事儿。
    彻底贯彻少既是多的思想
"""

import os, random


def run():
    # 常规生成一个List
    a_list = [i for i in range(0, 10)]
    print '常规生成list=', a_list
    # 生成一个空的List
    a_list = [0 for i in range(0, 11)]
    print '生成一个定值的list=', a_list
    # 生成一个含有运算的list
    a_list = [i * i for i in range(0, 11)]
    print 'i^2 list =', a_list
    # 生成一个带有判断的list
    a_list = [i for i in range(0, 20) if i % 2 == 0]
    print '0到19的偶数是：', a_list
    # 生成一个两层嵌套的list
    a_list = [m + n for m in '123' for n in '456']
    print '十位有123，个位由456组成的所有两位数：', a_list
    # 生成一个基于函数的List
    a_list = [random.randint(0, 10) for i in range(0, 10)]
    print '生成十个随机数：', a_list
    # 一个常用的列表生成式-查询某目录下的文件
    doc_local = 'h:\\BMI\\PythonExercise\\'
    a_list = [doc for doc in os.listdir(doc_local)]
    print doc_local + "目录下的文件有:", a_list
    print("hello")

if __name__ == "__main__":
    run()
