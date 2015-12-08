# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.08 22:16 

"""

"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""


def run():
    sn = float(100)
    num = 10
    distance = [sn]
    for i in range(0, num):
        sn /= 2
        distance.append(sn)
    total_distance = sum(distance[:]) + sum(distance[1:9])
    print distance
    print 'Total distance:' + str(total_distance)
    print("hello")


if __name__ == "__main__":
    run()
