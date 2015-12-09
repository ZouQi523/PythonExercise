# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.09 23:35 

"""

"""
题目：模仿静态变量的用法。
    1.类的私有变量
        在变量名前加__
        类的私有变量，外部无法直接访问
"""


def run():
    var = 0
    print 'var = %d' % var
    var += 1


class Static:
    __PrivatVar = 5
    PublicVar = 5
    def TryChangeStaticVar(self):
        self.__PrivatVar += 1
        self.PublicVar +=1
        print 'Private var =',self.__PrivatVar,'Public var=',self.PublicVar


if __name__ == "__main__":
    a = Static()
    for i in range(10):
        run()
        #a.__PrivatVar = 6#启用后程序报错
        a.PublicVar=5
        a.TryChangeStaticVar()
