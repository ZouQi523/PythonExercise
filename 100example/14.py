# coding: utf-8
"""
Created on 2015.12.06.14.33
__author__ = ZouQi
"""

"""
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
    1.理解print
        实际上使用pycharm的时候，IDE将print函数重定义了一下，或者理解为重新封装了一层
        所以在使用PYTHON的print时，会在后面自动为你添加一个换行符。
        但我们可以在程序中自己重定义print输出的地方。
        stdout相当于系统的管道，可以理解为一个指针。默认情况下系统将这个指针指向了，输出
        的窗体。而在这个程序当中，我们可以将这个指针执行一个文件。这样我们就可以将文件输出的内容
        进行保存了。
"""

import  sys
def run():
    data_str = ''
    data = int(raw_input(u'请输入要分解的数:'))
    for i in range(2, data + 1):
        while data != i:
            if data % i == 0:
                if len(data_str) != 0:
                    data_str += '*'
                data_str += str(i)
                data /= i
            else:
                break
    saveout =sys.stdout
    fsock =open('testStdout.txt','w')
    sys.stdout=fsock
    if len(data_str) != 0:
        print data_str + '*' + str(data)
    else:
        print str(data)


if __name__ == "__main__":
    run()
