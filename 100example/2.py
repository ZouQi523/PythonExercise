# -*- coding:utf-8 -*-
"""
Created on Tue Dec 01 23:42:45 21015

@author: zouqi
1222"""

"""
题目：企业发放的奖金根据利润提成。
    利润(I)低于或等于10万元时，奖金可提10%；
    利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，
可可提成7.5%；
    20万到40万之间时，高于20万元的部分，可提成5%；
    40万到60万之间时高于40万元的部分，可提成3%；
    60万到100万之间时，高于60万元的部分，可提成1.5%，
    高于100万元时，超过100万元的部分按1%提成，
    从键盘输入当月利润I，
求应发放奖金总数？

练习要点：
        1.使用中文字符时，因为使用了UTF-8编码，需要在中文字符串前 u
        2.try……except的使用
            2.1
            try成功后执行try以后的内容
            except 后执行except内容，而后执行之后的代码
            2.2
            错误的继承关系
            当不使用valueerror时输入中文，程序报错为unicodedecodeerror
            又因为unicodedecodeerror继承自valueerror
            故使用valueerror后即便报错中含有unicodedecodeerror也不会执行
            2.3错误日志的记录
            logging 记录错误，用到的时候再详细的写
        3.exit()
            退出程序
        4.测算程序执行效率
            使用time.clock函数获取起始时间戳和结束时间戳，相减获得程序执行效率
"""
import time
def InputData():
    data=raw_input(u'净利润：')
    try:
        data=int(data)
    except ValueError:
        print u'字符非法'
    return data
def examlp1(data):
    if data <= 100000:
        bonus = data*0.1
        return bonus
    if data <= 200000:
        bonus = 10000+(data-100000)*0.075
        return bonus
    if data <= 400000:
        bonus = (data - 200000)*0.05+17500
        return bonus
    if data <= 600000:
        bonus=(data-400000)*0.03+27500
        return bonus
    if data <=1000000:
        bonus=(data-600000)*0.015+33500
        return bonus
    if data > 1000000:
        bonus=(data-1000000)*0.01 +39500
        return bonus

#例程解题方法
def exampl2(i):
    arr = [1000000,600000,400000,200000,100000,0]
    rat = [0.01,0.015,0.03,0.05,0.075,0.1]
    r = 0
    for idx in range(0,6):
        if i>arr[idx]:
            r+=(i-arr[idx])*rat[idx]
            #print (i-arr[idx])*rat[idx]
            i=arr[idx]
    return r    
if __name__=='__main__':
    profit=InputData()
    starttime =time.clock()
    print u'邹琪算法，奖金：%d' % examlp1(profit)
    endtime=time.clock()
    print u'邹琪算法用时:'
    ZouTime=endtime-starttime
    print ZouTime
    starttime =time.clock()
    print u'例程算法，奖金：%d' % exampl2(profit)
    endtime=time.clock()
    print u'例程算法用时:'
    TYPETIME=endtime-starttime
    print TYPETIME
    if ZouTime>TYPETIME:
        print u'zou slow'
    else:
        print  'type slow'