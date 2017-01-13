#-*- coding:utf-8 -*-  
##################################################
#Filename: login.py                              #
#Revsion: 1.0                                    #
#Description login is test                       #
#Date: 2017/01/13                                #
#Auther: genglei                                 #
#Email: 18600517476@163.com                      #
##################################################

# 自己定义的用户名密码
import getpass #导入模块
_user = "genglei" 
_passwd = "abc123"
count = 0 #计数器 

while count <3:  #判断count是否大于3

    useradd = input("请输入用户名: ") #提示用户输入用户名名
    
    password = getpass.getpass("请输入密码: ")  #提示用户输入密码
    
    if useradd == _user and password == _passwd:  #判断用户输入的和自己定义的是否一致
        
        print ("欢迎登陆")
        break    #跳出循环
    
    else:
    
        print ("请检查用户名密码") #打印信息
        count += 1   #count=count+1 