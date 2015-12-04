# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 14:17:29 2015

@author: zouqi
"""
"""
题目：暂停一秒输出。
    1.time模块的使用
        1.1clock
            第一次调用获取一个时间戳
            第二次调用获取前面程序执行所用的时间

"""
import time

print time.time()
time.sleep(1)
print time.time()

print time.clock()
time.sleep(1)
print time.clock()
