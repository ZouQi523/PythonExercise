# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.22 14:00 

"""
"""
    OOP(object-oriented programming) <==> 面向对象编程
"""


# 创建一个汽车类 basic1
class car(object):
    pass  # pass 等价于 do nothing 旨在保证语法的完整性


# 继承一个汽车类 创建一个私有属性basic2
class largeFamilyCar(car):
    def __init__(self, name, colour):
        self.__name = name  # 加上下划线后，变成了私有属性，外部不可访问
        self.__colour = colour

    def pushCarInfo(self):
        print 'Car name:', self.__name, ' Colour :', self.__colour

    def set_name(self, name):  # 创建一个方法修改了类内部的属性
        self.__name = name

    def get_name(self):
        return self.__name

    def run(self):
        print self.__name, 'is running'


# 继承中级车的类 -basic 3
class executiveCar(largeFamilyCar):
    def run(self): #重写了父类的run方法。 需要注意的是父类的私有变量无法直接访问
        print self.get_name(),'is slowly runing'
    pass


def run():
    # basic1 为类动态绑定一个属性
    ExamplCar = car()  # 创建一个类的实例
    ExamplCar.name = 'BMW 523'
    print ExamplCar.name
    del ExamplCar

    # basic2 设置一个访问限制的变量
    ExamplCar1 = largeFamilyCar('BMW', "blue")
    ExamplCar1.pushCarInfo()
    ExamplCar1.set_name('Benze')
    ExamplCar1.pushCarInfo()

    # basic3 重载了一个父类的方法
    ExamplCar1.run()
    Examp2Car = executiveCar('Audi', 'black')
    Examp2Car.pushCarInfo()
    Examp2Car.run()


if __name__ == "__main__":
    run()
