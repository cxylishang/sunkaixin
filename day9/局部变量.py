#-*- coding:utf-8 -*-
# Author: li Shang

# school = "old boy"
# def change_name(name):
#     global school
#     school = "baoge edu"
#     print("before name:",name,school)
#     name = "LiShang"
#     print("after name:",name)
#
# name = "lishang"
# change_name(name)
# print("name:",name)
# print(school)

def change_name():
    global name
    name = "Lishang"

change_name()
print(name)