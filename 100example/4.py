# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 17:29:19 2015

@author: ZouQi
"""

"""
题目：输入某年某月某日，判断这一天是这一年的第几天？

"""
import re
def InputString():
    string=raw_input('Year.month,day:')
    try:
        data=string.split('.')
        if len(data) !=3:
            print 'error data'
            return False
        if str.isdigit(data[0]) and str.isdigit(data[1]) and str.isdigit(data[2]):
            Year=int(data[0])
            month=int(data[1])
            day=int(data[2])
            return Year,month,day
        else:
            print u'error data'
            return False
    except AttributeError:
        print u'error data'
        return False

if __name__ == '__main__':
    dat=False
    while dat==False:
        dat=InputString()
    print dat