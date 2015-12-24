# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.22 22:11 

"""

# Advanced 1 使用__slots__
"""
    当实例化一个类的时候，PYTHON会创建一个DICT来存放
    类的属性和方法，如果使用__slots__则可以dict
    创建所浪费的空间。当然使用这个可能会降低类的灵活性
"""

from types import MethodType
import random


class vehicle(object):
    # __slots__ = ('name', 'speed', 'print_vehicle_name')
    # Advanced 2 使用property <==>性质 属性
    """
    使用property可将方法变成属性调用，类似于装饰器（decorator）
    """

    @property
    def runWhere(self):
        return self._runWhere

    @runWhere.setter
    def runWhere(self, value):
        runWhereLimit = ['Land', 'Space', 'Water', 'Sky']
        if value in runWhereLimit:
            self._runWhere = value
        else:
            raise 'Value error in runwhere'

    """
    类的一些固定方法的使用
    """

    # Advanced 3-1 __str__的使用
    def __str__(self):
        return 'vehicle object(name=%s)' % self.name

    # __repr__=__str__

    # Advanced 3-2 __iter__ 让类变成一个可迭代的对象
    def __init__(self):
        self.count = 0
        self.speed = 0

    def __iter__(self):
        return self

    def next(self):
        self.speed = random.randint(0, 200)
        self.count += 1
        if self.count > 10:
            self.count = 0
            raise StopIteration
        return self.speed

    # Advanced 3-3 __getattr__ 用于处理动态增加的属性
    def __getattr__(self, item):
        if item == 'displacement':  # 动态增加的一个属性
            return '1.6'
        if item == 'go':  # 动态增加一个方法
            return lambda: 'go go go'

    pass


def print_vehicle_name(self):
    print 'vehicle name: ', self.name


def run():
    # Advanced 1 动态绑定方法的实现
    smart_car = vehicle()
    smart_car.name = 'smart car'
    smart_car.print_vehicle_name = MethodType(print_vehicle_name, smart_car, vehicle)  # 动态绑定一个方法
    smart_car.print_vehicle_name()

    # Advanced 2 使用Property
    smart_car.runWhere = 'Land'
    print smart_car.runWhere

    # Advanced 3-1
    print smart_car

    # Advanced 3-2
    for i in smart_car:
        print smart_car.name, ' speed: ', str(i)
    for i in smart_car:
        print smart_car.name, ' speed: ', str(i)

    # Advanced 3-3
    print 'Smart Car displacement:', smart_car.displacement
    print  smart_car.go()

    # Advanced 3-4动态创建一个类
    """
    x1x = type(x2x,x3x,x4x)
    x1x :类名
    x2x :继承的类名
    x3x :绑定的方法
    """

    def goup(self):
        return 'airplane go up'

    airplane = type('airplane', (vehicle,), dict(up=goup))
    smart_airplane = airplane()
    print smart_airplane.up()

    # Advanced 3-5 元类
    # 比较复杂等到用到的时候再来详细说明
if __name__ == "__main__":
    run()
