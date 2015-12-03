# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 17:26:37 2015

@author: ZouQi
"""

"""
题目：斐波那契数列
    0,1,1,2,3,5,8
    	1.一种奇妙的写法
		"a,b=b,a+b"
		状态1：a=1,b=2
		运行a,b=b,a+b一句后
		状态2：a=2,b=3
		由结果反推回运算过程
		当计算机执行这句话时，实际上已经将a,b缓存起来
		a=状态1的b <==>2
		b=状态1的a+b <==>1+2
		运用该方法可实现等差数列
			a,b=0,2
			a,b=b,b+2
	2.第一次使用递归
		可以把它理解成是一种逆向思维。
		比如你想求解第10个数，那么你就要知道第9个和第8个数
		如果你想知道第9个数，那么你就要知道第8个和第7个数
		如果你要知道第8个数，那么你要知道第7个和第六个数
		以此类推
		你知道第1个数是1，第二个数是也是1。由此就可以反推回去了
"""

def example1():
    data=raw_input()
    data=int(data)
    l=[0,1]
    for i in range(data-1):
        l.append(l[-1]+l[-2])
    print l
def example2():
    data=raw_input()
    data=int(data)
    a,b = 1,1
    for i in range(data-1):
        a,b = b,a+b
    print a   
def example3():
    data=raw_input()
    data=int(data)
    def fib(n):
        if n==1 or n==2:
            return 1
        return fib(n-1)+fib(n-2)
    print fib(data)
if __name__ == '__main__':
    #example1()
    #example2()
    example3()