# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.08 08:35

"""

"""
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
"""

def run():
    for j in range(2,1001):
        k = []
        n = -1
        s = j
        for i in range(1,j):
            if j % i == 0:
                n += 1
                s -= i
                k.append(i)

        if s == 0:
            print j
            print str(k[:])

if __name__ == '__main__':
    run()
