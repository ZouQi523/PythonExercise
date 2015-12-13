# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.13 17:39 

"""
"""
    Advanced feature    <==>高级特性
    Interation          <==>迭代
    详细内容参见，廖雪峰教程中的迭代。
"""


def run():
    # 常用数据类型的迭代-list
    a_list = [1, 2, 3, 4, 5, 6, 7]
    for i in a_list:
        print i
    # list的二维数组
    a_list = [(1, 2), (3, 4), (5, 6)]
    for i, i1 in a_list:
        print i, i1

    # 常用数据类型的迭代-dict
    d_dict = {'a': 1, 'b': 2, 'c': 3}
    # dict迭代输出key
    for key in d_dict:
        print 'dict key =', key
    # dict迭代输出value
    for value in d_dict.itervalues():
        print 'dict value=', value
    # dict迭代输出key与value
    for key, value in d_dict.items():
        print 'dict key=', key, 'value=', value

    #常用数据类型的迭代-字符串
    c_str='lastweek I went to the theater'
    for letter in c_str:
        if letter > 'e':
            print letter+' Letter \'ASCII value >e'
    #字符串在某一区内索引
    for letter in c_str[:4]:
        if letter > 'e':
            print letter+' Letter \'ASCII value >e'

    #迭代技巧-使用索引对象的下标
    for i,value in enumerate(c_str):
        print i,value
    print("hello")


if __name__ == "__main__":
    run()
