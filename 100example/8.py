# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 23:11:29 2015

@author: zouqi
"""

"""
题目：输出9*9乘法口诀表。
	1.递归实现
		example1使用了递归实现九九乘法表。使用递归的核心思想，就在于
		你得知道在最核心那一层你要做什么事情
	2.如何让python的print不换行
		在结尾加上‘,’即可。记住要加在pirnt表达式的结尾哦
"""
def example():
    for a in range(1,9):
        for b in range(1,9):
            print"%d * %d = %d " % (a,b,a*b),
def example1(arg):
    if arg == 1:
        print '1 * 1 = 1'
        return 1 
    for i in range(1,arg):
        print "%d * %d = %d " % (i,arg,i*arg),
    print '\r\n',
    arg=arg-1
    return example1(arg)
if __name__ =='__main__':
    example1(9)