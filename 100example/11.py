# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 14:17:29 2015

@author: zouqi
"""
"""
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
    假如兔子都不死，问每个月的兔子总数为多少？
    1   2   4   8   16  32
        1.在python中如何实现平几次方
            使用**
"""
def rabbit(total_month):
    """
    用于计算兔子的总量
    :param total_month:兔子生存的月份
    :return rabbit_num_list:
    """
    start_num=1 #初始兔子种群的数量
    rabbit_num_list=[]
    for i in range(total_month):
        if i%3 == 0:
            start_num=2**(int(i/3))
            rabbit_num_list.append(start_num)
        else:
            rabbit_num_list.append(rabbit_num_list[-1])
    return rabbit_num_list
if __name__ == '__main__':
    print rabbit(10)