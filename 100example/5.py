# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 16:54:31 2015

@author: ZouQi
"""

"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
	1.尝试使用了list
		使用了append方法。想表的结尾添加一个元素
		使用了sort方法，将表排序
"""
l=[]
def exampl1():
    data=raw_input(u'请输入数字：')
    if data == 'exit':
        return True
    if str.isdigit(data) == False:
        return False
    data=int(data)
    l.append(data)
    list.sort(l)
    print l
    return False

if __name__ == '__main__':
    status =False
    while status == False:
        status = exampl1()