# -*- coding:utf-8 -*-
"""
Created on Tue Dec 01 23:42:45 21015

@author: zouqi
"""

"""
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，
可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，
可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，
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
"""

def examlp1():
    data=raw_input(u'净利润：')
    try:
        data=int(data)
        print data
    except(ValueError):
        print u'字符非法'
        exit()
    
if __name__=='__main__':
    examlp1()