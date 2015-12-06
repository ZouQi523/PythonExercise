# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 14:17:29 2015

@author: zouqi
"""
"""
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
    假如兔子都不死，问每个月的兔子总数为多少？
    1   2   4   8   16  32
    1   2   3   4   5   6   7   8   9   10
    1   1   2   3   5   8
    使用数组描述兔子生存过程
    1:1 0 0 <==>1
    2:0 10  <==>1
    3:1 0 1 <==>2
    4:1 1 1 <==>3
    5:2 1 2 <==>5
    6:3 2 3 <==>8
    7:5 3 5 <==>13

        1.在python中如何实现平几次方
            使用**
"""
def rabbit(total_month):
    """
    用于计算兔子的总量
    :param total_month:兔子生存的月份
    :return rabbit_count_num_list:
    """
    aduit_num=0 #初始兔子种群的数量
    nonage_num=1
    rabbit_num_list=[1,0,0]
    rabbit_count_num_list=[]
    for i in range(total_month):
        a=rabbit_num_list[1]+rabbit_num_list[2]
        b=rabbit_num_list[0]
        c=rabbit_num_list[1]+rabbit_num_list[2]
        rabbit_num_list=[a,b,c]


        rabbit_count_num_list.append(sum(rabbit_num_list[:]))
    return rabbit_count_num_list
if __name__ == '__main__':
    print rabbit(21)