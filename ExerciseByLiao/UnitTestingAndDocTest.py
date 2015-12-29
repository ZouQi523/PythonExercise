# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.28 23:26 

"""

"""
    单元测试与文档测试
"""

# 单元测试
import unittest


class Dict(dict):
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


"""
1.以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
2.单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
"""


class TestDict(unittest.TestCase):
    def setUp(self):
        print 'setUp...'

    def tearDown(self):
        print 'tearDown...'

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d.ditc))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


# 文档测试
# 1.注意在>>>后面要跟一个空格，否则不能运行哦
# 2.如果文档测试通过了，则命令行内不会有内容哦
class People(object):
    """
    Example:
    >>> China = People()
    >>> China.WhereAreYouFrom()
    1
    """

    def WhereAreYouFrom(self):
        print '1'


def run():
    print("hello")


if __name__ == "__main__":
    import doctest

    doctest.testmod()#执行文档测试
    usa = People()
    usa.WhereAreYouFrom()
    run()
    # unittest.main()
