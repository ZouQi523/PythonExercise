# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.25 00:40 

"""
# 错误处理使用Try except finally
# 在这里不做详细论述

# 调试的三种方式
"""
1.print
2.assert    抛出错误
3.logging   不会抛出错误，会记录错误
    3.1 默认情况下日志级别是Warning
        日志级别关系：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
                        临界      错误     警告    信息     调试
"""
import logging

def run(value):
    logging.warning('This is warning message')
    try:
        v = int(value)
        assert v != 0, '数值非法'
    except ValueError:
        print 'ValueError 请输入数字'
    finally:
        print '输入结束'


if __name__ == "__main__":
    run('10')
    run('ssss')
