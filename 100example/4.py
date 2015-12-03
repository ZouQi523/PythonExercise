# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 17:29:19 2015

@author: ZouQi
"""

"""
题目：输入某年某月某日，判断这一天是这一年的第几天？
	1.map的用法
		简单来讲就是对一个LIST或其他的变量，执行同一个操作。如同代码第
		35到39行所显示的一样。同样是将字符串转换为INT型，直接调用MAP
		可是让代码变的清爽许多
	2.该程序的弱点
		在两个参数之间，只用了DATA来传递数据，而数据的结构在参数位置是
		不可见的。这将不利于多人开发。具体改进的方法还要在后继的学习中		
      体现出来
	3.dict的第一次尝试
     第一次尝试使用了数据字典。字典使用KEY作为索引，搜索指定的键值.
     需要特别强调的一点！！！字典内部的数据本身是无序的，将字典类型		
     的数据转换为一个list，无论是将KEY转换或者VALUE转换，转换完的结		
     果都是无序的    

"""
month_day_dict={'1':31,
                '2':28,
                '3':31,
                '4':30,
                '5':31,
                '6':30,
                '7':31,
                '8':31,
                '9':30,
                '10':31,
                '11':30,
                '12':31,}
month_day_list=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def InputString():
    string=raw_input('Year.month,day:')
    try:
        data=string.split('.')
        if len(data) !=3:
            print 'error data'
            return False
        if str.isdigit(data[0]) and str.isdigit(data[1]) and str.isdigit(data[2]):
           
            #Year=int(data[0])
            #month=int(data[1])
            #day=int(data[2])
            #data=map(int,data)
            return data
        else:
            print u'error data'
            return False
    except AttributeError:
        print u'error data'
        return False
def leap_check(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True   # 整百年能被400整除的是闰年
            else:
                return False
        else:
           return True       # 非整百年能被4整除的为闰年
    else:
       return False

def legal_check(data):
    if data == False:
        return False
    try:
        if int(data[1])<1:
            print 'legal error 1'
            return False
        if month_day_dict[data[1]] >= 2:
            if leap_check(int(data[0])):
                month_day_list[2]=29
          
        if month_day_dict[data[1]]<int(data[2]):
            print 'legal error'
            return False
        else:
            month_day_list[int(data[1])]=int(data[2])
            print 'day Numis %d' % sum(month_day_list[0:int(data[1])+1])
            return True
    except KeyError:
        print 'legal error 3'
        return False
if __name__ == '__main__':
    dat=False
    while dat==False:
        dat=InputString()
        dat=legal_check(dat)
