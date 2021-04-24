import json
import os
def main():
    print("+-------------------------------------------+")
    print("|  1)添加学生信息                           |")
    print("|  2)显示所有学生的信息                     |")
    print("|  3)删除学生信息                           |")
    print("|  4)修改学生信息                           |")
    print("|  5)按学生成绩（倒叙）显示学生信息         |")
    print("|  6)保存学生信息到文件（students.txt）     |")
    print("|  7)从文件中读取数据（students.txt）       |")
    print("|                                           |")
    print("|  退出：quit<回车>                         |")
    print("+-------------------------------------------+")
    student_info = []
    while True:
        try:
            i=int(input(''))
        except Exception as e:
                print("程序已退出")
                return
                 
        if not i: # 名字为空　跳出循环
            break
       
        elif i == 1 :
            student_info.append(add_student_info())
        elif i == 2 :
            show_student_info(student_info)
        elif i == 3:
            try:
                student_info.remove(del_student_info(student_info))
                print("删除成功")
            except Exception as e:
                print(e) 
        elif i == 4:
            try:
                info = mod_student_info(student_info)
                student_info.remove(del_student_info(student_info,del_id = info.get("id"))) 
                student_info.append(info)
            except Exception as e:
                print(e)
        elif i == 5:
            source_reduce(student_info)
        elif i == 6 :
            save_info(student_info)
        elif i == 7:
            read_info()
            student_info = read_info()
            print("读取成功")
        else :
            print("输入有误，请重新输入")
            continue

#1）添加学生信息
def add_student_info():
    while True:
        n = input("请输入编号：")
        if not n: # 名字为空　跳出循环
            break
        try:
            a = (input("请输入姓名："))
            x = int(input("请输入年龄："))
            y = input("请输入性别：")
            s = int(input("请输入成绩："))
        except:
            print("输入无效，不是整形数值．．．．重新录入信息")
            continue
        info = {'id':n,'name':a,'age':x,'sex':y,'score':s}
        print("学生信息录入完毕！！！")
        break
    return info

#2)显示所有学生的信息
def show_student_info(student_info):
    if not student_info:
        print("无数据信息．．．．．")
        return
    print("编号".center(2),"姓名".center(8),"年龄".center(4),"性别".center(4),"成绩".center(4))
    for info in student_info:
        print(str(info.get('id')).center(4),info.get('name').center(8),str(info.get('age')).center(8),info.get('sex').center(4),str(info.get('score')).center(8))

#3）删除学生信息
def del_student_info(student_info,del_id = ''):
    if not del_id:
        del_id = input("请输入删除的学生编号：")
    for info in student_info:
        if del_id == info.get("id"):
            return info
    raise IndexError("学生信息不匹配,没有找到%s" %del_id)

#4）修改学生信息
def mod_student_info(student_info):
    mod_id = input("请输入修改的学生编号：")
    for info in student_info:
        if mod_id == info.get("id"):
            a = (input("请输入姓名："))
            x = int(input("请输入年龄："))
            y = input("请输入性别：")
            s = int(input("请输入成绩："))
            info = {'id':mod_id,'name':a,'age':x,'sex':y,'score':s}
            print("成功修改编号为"+str(mod_id)+"的学生信息")
            return info
    raise IndexError("学生信息不匹配,没有找到%s" %mod_id)

#5）按学生年龄高－低显示学生信息
def source_reduce(student_info): 
    print("按学生成绩倒叙显示：")
    mit = sorted(student_info ,key=lambda x:x["score"])
    show_student_info(mit)

#6）保存学生信息到文件（students.txt)
def save_info(student_info):
    js = json.dumps(student_info) 
    try:
        file = open('students.txt', 'w')
    except Exception as e:
        students_txt = open("students.txt", "x") # 文件不存在，创建文件并打开
    file.write(js) 
    file.close()    
    print("保存成功")
  
#7）从文件中读取数据（students.txt) 
def read_info():
    try:
        file = open('students.txt', 'r') 
    except Exception as e:
        print("读取失败")
    js = file.read()
    dict = json.loads(js)
    file.close()
    return dict

main()