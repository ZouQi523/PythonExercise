#coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.07 22:37 

"""
"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制
    1.lambda
        什么时候用？
            当一些地方需要一个函数来操作，但只有此处调用该函数的时候
            省去给函数起名字的困扰
            使程序更为简洁
    2.reduce
        reduce函数即为化简，它是这样一个过程：
        每次迭代，将上一次的迭代结果（第一次时为init的元素，如没有init则为seq的第一个元素）
        与下一个元素一同执行一个二元的func函数。
        在reduce函数中，init是可选的，如果使用，则作为第一次迭代的第一个元素使用。
        0   1   2   3   4
        |   |   |   |   |
          x     2   |   |
             x1     3   |
                x2      4
                    x3
        简单来说就是下面这个例子
        reduce( func, [1, 2,3] ) = func( func(1, 2), 3)
"""
def new_num(count,num):
    """
    用于生成新的Num
    :param count: 生成Num的位数
    :param num:旧的Num
    :return data: 新的Num
    """
    data=0
    for i in range(count):
        data+=num*10**i
    return data
def run():
    num = int(raw_input('Num='))
    count = int(raw_input('Count='))
    num_list=[]
    for i in range(1,count+1):
        num_list.append(new_num(i,num))
    print num_list
    print sum(num_list[:])
    Sn = reduce(lambda x,y : x + y,num_list)
    print Sn

if __name__ == "__main__":
    run()