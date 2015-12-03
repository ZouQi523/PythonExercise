# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 22:45:06 2015

@author: zouqi
"""

"""
题目：将一个列表的数据复制到另一个列表中。
	1.list与C语言数组的不同
		C语言的数组是一种更紧密的数据结构，当存储一种类型的数据时，
		内存分配也是按照该种数据类型进行分配
		而Python的list则是一种更为灵活的数据结构，直观的感受是，其既
		可以存放整数，也可存放字符串。
		虽然C语言的的数据也可实现类似的功能。但其复杂程度非常大。可见
		python的解释器，还是不赖的
	2.注意第37行和第41行的区别
		具体有啥不同，相信试验过一次后，大家就清楚了
"""
a_list=[1,2,3,4,5,6,7,8,9,'10','11','12']

#copy to a list
b_list=a_list[:]
print 'Copy to b_list ='+str(b_list)

#the elements of copy from 0 to 5
b_list=a_list[:5]
print 'copy from 0 to 5 to b_list ='+str(b_list)

#Copy from the bottom of 1 to 5 elements to b
b_list=a_list[-5:-1]
print 'Copy from the bottom of 1 to 5 elements to b ='+str(b_list)

#Delete from 1 to 5 elements to b
b_list=a_list[:]
del b_list[1:5]
print 'Delete from 1 to 5 elements to b ='+str(b_list) 

#at the end add a element
b_list=a_list[:]
b_list.append('I\'m the Append')
print 'at the end add a element to b ='+str(b_list) 

b_list=a_list[:]
b_list[0:3]=['n','e','w']
print str(b_list)

b_list=a_list[:]
b_list[0:4]=['n','e','w']
print str(b_list)