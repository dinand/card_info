'''
Created on 2018-1-22

@author: zhaocq
'''
#!/usr/bin/python3
# -*- coding: UTF-8 -*-

card_infors = []

def print_menu():
    """ 完成打印功能菜单 """
    print("="*50)
    print("        名片管理系统 V0.01")
    print("1.添加一个新的名片")
    print("2.删除一个名片")
    print("3.修改一个名片")
    print("4.查询一个名片")
    print("5.显示所有的名片")
    print("6.保存信息")
    print("7.退出系统")
    print("="*50)

def add_new_card_info():
    """ 完成添加一个新的名片 """
    new_name = input("请输入新的名字:")
    new_qq = input("请输入新的QQ:")
    new_weixin = input("请输入新的微信:")
    new_addr = input("请输入新的地址:")
    #定义一个新的字典，用来存储一个新的名片
    new_info = {}
    new_info['name'] = new_name
    new_info['qq'] = new_qq
    new_info['weixin'] = new_weixin
    new_info['addr'] = new_addr
    #将一个字典 添加到列表中
    global card_infors
    card_infors.append(new_info)
    #print(card_infors) #for test

def find_card_infor():
    """ 用来查询一个名片 """
    global card_infors
    find_name = input("请输入要查找的姓名")
    find_flag = 0 #默认表示没有找到
    for temp in card_infors:
        if find_name == temp['name']:
            print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['weixin'],temp['addr']))
            find_flag = 1 #表示找到了
            break
    #判断是否找到了
    if find_flag == 0:
        print("查无此人")

def show_all_info():
    #""" 显示所有的名片信息 """
    global card_infors
    print("姓名\tQQ\t微信\t住址")
    for temp in card_infors:
        print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['weixin'],temp['addr']))

def save_2_file():
    """ 把已经添加的信息保存到文件中 """
    f = open("backup.data", "w")
    f.write(str(card_infors)) #要列表  以字符串的形式写入 （列表写入会报错）
    f.close()

def load_info():
    global card_infors
    try:
        f = open("backup.data")  #默认只读模式
        #card_infors =  list(f.read())  #会报错
        card_infors =  eval(f.read()) #文件不大可以直接用read ,如果量大就不能用read ,eval是会转成字符串之前的格式
        f.close()
    except Exception:
        pass

def main():
    """ 完成对整个程序的控制 """

    #恢复（加载）之前保存的数据信息
    load_info()

    # 1 打印功能提示
    print_menu()
    while True:
        #2.获取用户的输入
        num = int(input("请输入操作序号:"))
        #3.根据用户的数据执行相应的功能
        if num == 1:
            add_new_card_info()
        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            find_card_infor()
        elif num == 5:
            show_all_info()
        elif num == 6:
            save_2_file()
        elif num == 7:
            break
        else:
            print("输入有误请重新输入")
        print("")


if __name__ == "__main__":
    #调用主函数
    main()

