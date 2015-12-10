#coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.10 22:42 

"""
"""
题目：学习使用自建模块
    1.创建module目录
    2.在目录下创建__init__.py 文件可为空
    3.使用该包时候使用from指向地址，导入模块
    详细内容参见：http://www.cnpythoner.com/post/2.html
"""
from test44_package import test44Module
from test44_2package import test44Module2
def run():
    print("hello")
    b=test44Module
    test44Module.SayModule()
    test44Module2.SayIm2module()

if __name__ == "__main__":
    run()