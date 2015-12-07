# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.06.23.27 

"""
"""
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
    1.Python不支持标准C的三目运算符
        用Python自制的实现方式是 A if 条件 else B
"""
import random


def run():
    grade = []
    score_list = [random.randint(0, 100) for i in range(0, 10)]  # 随机生成是十个人的成绩
    for i in range(10):
        # grade[-1]=score_list[i]>90 ? 'A':(score_list[i]>60 ? 'B':'C')
        data = 'A' if score_list[i] > 90 else('B' if (score_list[i] > 60) else 'C')
        grade.append( data )
    print score_list
    print grade
if __name__ == "__main__":
    run()
