# coding: utf-8
"""
__author__ = ZouQi
Created on 2015.12.07 18:51

"""

"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
    1.遍历字典
        adict.keys() 返回一个包含字典所有KEY的列表；
        adict.values() 返回一个包含字典所有value的列表；
        adict.items() 返回一个包含所有（键，值）元祖的列表；
        其中adict为字典的名称
    2.处理中英混排的字符串
        首先将字符串经过unicode编码，使其等长，在进行处理。
"""
def is_chinese(uchar):
    """
    :param uchar:输入一个字符
    :return: True 为汉字 False其他
    """
    if uchar >= u'/u4e00' and uchar<=u'/u9fa5':
        return True
    else:
        return False

def run():
    Count_dict={u"数字:":0,
                u"字母:":0,
                u"中文:":0,
                u"空格:":0}
    string = raw_input(u'请输入字符串：')
    string =unicode(string,'utf-8')
    print type(string)
    for i in string:
        if i.isdigit():
            Count_dict[u"数字:"] += 1
        elif is_chinese(i):
            Count_dict[u"中文:"] += 1
        elif i.isalpha():
            Count_dict[u"字母:"] += 1
        elif i.isspace():
            Count_dict[u"空格:"] += 1


    for item,value in Count_dict.items(): print '%s%s' % (item, value)


if __name__ == '__main__':
    run()