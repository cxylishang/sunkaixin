#-*- coding:utf-8 -*-
# Author: li Shang

# def test(*args):
#     print(args)
#
# test(1,2,3,4,5)
# test(*[1,2,3,4,5,])     #也可以按照*[]，*跟元组的方式传递
#
#
# def test1(x, *args):
#     print(x)
#     print(args)
#
# test1(1, 2, 3, 4, 5, 6, 7)

# def test2(**kwargs):
# 	print(kwargs)
# test2(name='lishang',age=23,sex='man')
# test2(**{'name':'xiaomeng','age':18,'sex':'girl'})     #也可以按照**{}，**跟字典的方式传递

# def test3(name, **kwargs):
#     print(name)
#     print(kwargs)
#
# test3('lishang',age=18,girlfriend='zhaoxiaomeng')
#
# def test4(name,age=18,**kwargs):
#     print(name)
#     print(age)
#     print(kwargs)
#
# test4('xiaomeng', sex='girl', hobby='lishang')

def logger(source):
    print("from %s"%source)

def test5(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("test5")

test5('xiaomeng',24,'she likes Lishang',sex='girl',hobby='lishang')

