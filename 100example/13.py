# coding: utf-8
"""
Created on 2015.12.06.14.33
__author__ = ZouQi
"""

"""
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
    1.请注意使用的提取每位数字的方法
"""
def run():
    for n in range(100,1000):
        i = n / 100
        j = n / 10 % 10
        k = n % 10
        if n == i ** 3 + j ** 3 + k ** 3:
            print n


if __name__ == "__main__":
    run()
