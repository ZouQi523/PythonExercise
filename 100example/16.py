# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.07 18:33

"""
"""
题目：输出指定格式的日期。
"""
import datetime


def run():
    print datetime.date.today().strftime('%d/%m/%Y')


    # 创建日期对象
    miyazakiBirthDate = datetime.date(1941, 1, 5)
    print(miyazakiBirthDate.strftime('%d/%m/%Y'))

    # 日期算术运算
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

    # 日期替换
    miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)
    print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))
    print miyazakiBirthDate.weekday()
    print 'hello world'
if __name__ == '__main__':
    run()
