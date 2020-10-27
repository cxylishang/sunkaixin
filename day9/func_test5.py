#-*- coding:utf-8 -*-
# Author: li Shang

def test(x,y):          #x,y是形参
    print(x)
    print(y)

test(3,2)               #位置参数调用,实参与形参一一对应
test(y=3,x=4)           #关键字调用
test(1,y=2)             #两种混合,关键字调用必须在后面
#test(x=1,2)x