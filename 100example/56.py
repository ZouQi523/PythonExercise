# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.12 09:04 

"""

"""
题目：画图，学用circle画圆形。
    1.调整颜色
        使用字符串   '#FFF'表示白色
                    '#000000'表示黑色
    2.参考的说明手册
        http://effbot.org/tkinterbook/canvas.htm
"""


def run():
    print("hello")


class BackgroudColor:
    def __init__(self):
        pass

    White = '#FFF'
    Black = '#000000'


if __name__ == "__main__":
    from Tkinter import *

    canvas = Canvas(width=800, height=600, bg=BackgroudColor.White)
    canvas.pack(expand=YES, fill=BOTH)  # 将Canvs添加到主窗口
    """
    绘制一个复杂图形
    重心 x,y=400,300
    """
    x, y = 400, 300
    R = 200
    # 绘制圆形
    canvas.create_oval(x - R, y - R, x + R, y + R, width=1)
    # 绘制一个外接圆形的正方形
    canvas.create_rectangle(x - R, y - R, x + R, y + R, width=1)
    # 绘制直线
    line = canvas.create_line(x, y, x + R, y + R, fill='red', width=1)  # 可见这样创建，是创建了一个组建
    canvas.delete(line)  # 在这里输入组建的名称，即可将这个组建删除
    run()
    mainloop()
