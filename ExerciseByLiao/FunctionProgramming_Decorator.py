# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.17 10:45

"""

"""
    Decorator <==> 装饰器
    在不改变原有函数的情况下，增强这个函数原有的功能
    1.装饰器这个东西到底有卵用？
        详细的说明，可参见：http://www.cnblogs.com/rollenholt/archive/2012/05/02/2479833.html
        网址里面举得例子是，当你想测试一个函数的执行效率，又不想在现有工程上删除任意一行代码
        应该如何实现？
        那么就要用装饰器了。
        有个函数叫A，他能做一件了不起的事儿。
        在他做之前，我想让A君先做一件别的事儿，然后在做了不起的事儿，在做一件事儿。要怎么做？
        方法一：
        写一个函数B
        然后B（A）
        这样弄了以后，你的主函数是不是也跟着变了？
        方法二：
        写一个装饰器B_Decorator
        然后再A君前面加上一行@B_Decorator
        酷！在你不变的主程序中，你执行A君的时候。那么他就会跳到@B_Decorator去执行。
"""


# 不带参数的装饰器例子
def log(func):
    def wrapper(*args, **kw):
        # print '我被增强了'
        return func(*args, **kw)

    print '我被增强了'
    return wrapper


@log
def run():
    print 'hello world'


# 带参数的例子


def deco(func):
    def _deco(a, b):
        print("1before myfunc() called.")
        ret = func(a, b)
        print("  3after myfunc() called. result: %s" % ret)
        return ret

    return _deco


@deco
def myfunc(a, b):
    print(" 2myfunc(%s,%s) called." % (a, b))
    return a + b


# 自己写一个装饰器的例子

def TimeAndAddress(func):
    def _TimeAndAddress(why, time='', address=''):
        print 'in ', time
        func(why)
        print 'at ', address

    return _TimeAndAddress


@TimeAndAddress
def ImAlone(why=''):
    print 'I\'m alone', why


if __name__ == '__main__':
    # 函数也是一个对象
    w = run  # 将函数赋值一个参数
    w()  # 执行这个函数
    print w.__name__  # 打印函数对象的名字，此时函数的名称已经变成了wrapper，即增强过的名字
    myfunc(1, 2)
    ImAlone(why='no why')
    print ImAlone.__name__

