# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 17:29:19 2015

@author: ZouQi
"""

"""
题目：输入某年某月某日，判断这一天是这一年的第几天？

"""
month_day_dict={'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31,}
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
def leap_check(data):
    return True
def legal_check(data):
    try:
        if int(data[0]<=0):
            return 'legal error'
        if month_day_dict[data[1]] >= 2:
            month_day_dict['2']=29
            
        if month_day_dict[data[1]]>int(data[2]):
            print 'legal error'
            return False
    except KeyError:
        print 'legal error'
        return False
if __name__ == '__main__':
    dat=False
    while dat==False:
        dat=InputString()
    print type(dat[0])
    print dat