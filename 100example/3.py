# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 16:36:35 2015

@author: ZouQi
"""
"""
题目:一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

完全平方数的含义：如：0，1，4，9，16，25，36，49等
设一个自然数x 其完全平方数等于 x^2

	1.使用str.isdigit()
		判断一个字符串是否为数字
		注意：使用这个只能判断，并不能进行类型转换

"""
import math
def InputData():
    data=raw_input(u'请输入数字：')
    if str.isdigit(data):
        return int(data)
    else:
        print u'请重新输入'
        return False

if __name__=='__main__':
    SearchRange=False
    while SearchRange == False:
        SearchRange=InputData()
    print type(SearchRange)
    
    for i in range(1,SearchRange):
        temp100 =math.sqrt(i+100)
        temp168 =math.sqrt(i+268)
        if temp100 == int(temp100) and temp168 == int(temp168):
            print 'This num is %d' % i
            