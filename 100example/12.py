# coding: utf-8
"""
Created on 2015.12.06.14.33
__author__ = ZouQi
"""

"""
题目：判断101-200之间有多少个素数，并输出所有素数。
    判断素数可做如下优化：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
    如果能被整除，则表明此数不是素数，反之是素数。
"""
prime_numer=[]
for i in range(101,200):
    for i1 in range(2,i):
        if i%i1 ==0:
            break
    if i1 == i-1:
        prime_numer.append(i)
print prime_numer