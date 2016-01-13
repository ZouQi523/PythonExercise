# coding: utf-8
"""
__author__ = ZouQi
Created on 2016.01.06 22:55 

"""

"""
    IO_Programming <==> IO编程
"""
import os


def run():
    # 标准的文件读取形式
    with open('H:\BMI\PythonExercise\ExerciseByLiao\ReadMe.txt', 'r') as f:
        print f.read()
        print f.tell()
        print("hello")
    f.close()

    # 读取文件中的指定字节数
    # 当读取较大的文件时，使用这种方法，否侧会一次沾满内存
    with open('H:\BMI\PythonExercise\ExerciseByLiao\ReadMe.txt', 'r') as f:
        print f.read(21)
        print f.read(21)
        print 'End0'

    # 读取文件中的一行
    with open('H:\BMI\PythonExercise\ExerciseByLiao\ReadMe.txt', 'r') as f:
        print f.readline()
        print f.readline()
        print 'End1'

    # 通过二进制读取文件中的内容(rb)
    # 该方法用于读取图片视频等数据
    with open('H:\BMI\PythonExercise\ExerciseByLiao\TestImage.jpg', 'rb') as f:
        print f.read()
        print 'End2'

    # 写文件
    with open('H:\BMI\PythonExercise\ExerciseByLiao\TestTxt.txt', 'w') as f:
        f.write('This\'s a test doc')
    with open('H:\BMI\PythonExercise\ExerciseByLiao\TestTxt.txt', 'r') as f:
        print f.read()
        print 'End3'

    # 操作文件和目录
    # 1.获取当前运行的是什么系统
    #   posix 表示是linux Unix Mac OS 其中之一
    #   nt    表示是windows
    print os.name
    # 2.获取环境变量
    print os.environ
    print os.getenv('PATH')  # 获取指定的环境变量
    # 3.查看当前目录的绝对路径
    path = os.path.abspath('.')
    print path
    # 4.在该目录下创建一个新的文件夹
    path += '/testDIR'
    print path
    try:
        os.mkdir(path)  # 当创建一个文件失败，返回183错误时，说明该文件夹已经被创建
    except WindowsError:
        # 5.删除一个文件夹
        os.rmdir(path)
    # 序列化
    # 将内存上的数据保存或用于传输的一个过程
    try:
        import cPickle as pickle  # 使用C语言序列化的实现，速度较快
        print 'cPickle'
    except ImportError:
        import pickle  # 使用Python实现的序列化，速度较慢

    d = dict(name='zouqi', age=28)
    pickleString = pickle.dumps(d)  # 将d内保存的内容序列化
    print pickleString
    # 将序列化的内容保存进文档
    os.remove('H:\BMI\PythonExercise\ExerciseByLiao\dump.txt')
    with open('H:\BMI\PythonExercise\ExerciseByLiao\dump.txt', 'wb') as f:
        pickle.dump(d, f)  # 将d的内容序列化保存进dump.txt
        print 'Save d to dump.txt'

    # 读取反序列化后的内容
    with open('H:\BMI\PythonExercise\ExerciseByLiao\dump.txt', 'r') as f:
        c = pickle.load(f)
        print c

    # 使用JSON结构
    import json
    if os.path.exists('H:\BMI\PythonExercise\ExerciseByLiao\dumpJson.txt'):
        os.remove('H:\BMI\PythonExercise\ExerciseByLiao\dumpJson.txt')
    with open('H:\BMI\PythonExercise\ExerciseByLiao\dumpJson.txt', 'wb') as f:
        Djson = dict(hp=100, skill='bite')
        json.dump(Djson, f) #序列化为JSON结构
    with open('H:\BMI\PythonExercise\ExerciseByLiao\dumpJson.txt', 'r') as f:
        Cjson = json.load(f) # 从json结构变回Python的字典
        print Cjson


if __name__ == "__main__":
    run()
