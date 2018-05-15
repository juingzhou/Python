def print_menu():
    print('*'*30)
    print("学生管理系统".center(30))
    print("输入1：添加学生")
    print("输入2：查找学生")
    print("输入3：修改学生")
    print("输入4：删除学生")
    print("输入5：查看所有学生")
    print("输入6：退出")

def add_student():
    name = input("请输入学生的姓名：")
    age = int(input("请输入学生的年龄："))
    qq = input("请输入学生的qq号：")
    stu={}
    stu["name"] = name
    stu["age"] = age
    stu["qq"] = qq
    stus.append(stu)
    print("添加成功！")

def serach_student(search_item):
    for item in stus:
        if item["name"] == search_item:
            print("%s 学生存在"%(search_item))
            print("姓名\t年龄\tqq号")
            print_student(item)
            break
    else:
        print("%s 学生不存在"%(search_item))
def print_student(item):
        print("%s\t%s\t%s"%(item["name"],item["age"],item["qq"]))
def print_all_students():
    print("序号\t姓名\t年龄\tqq号")
    for i,item in enumerate(stus,1):
        print("%s\t"%(i),end='')
        print_student(item)
def del_student(del_name):
    for item in stus:
        if del_name == item["name"]:
            stus.remove(item)
            print("删除成功！")
            break
    else:
        print("%s 学生不存在"%(del_name))

stus=[]
if __name__ == "__main__":
    while True:
        print_menu()
        operate=int(input("请输入你的想要的操作："))
        if operate==1:
            add_student()
        elif operate==2:
            name = input("请输入你要查找的学生：")
            serach_student(name.strip())
        elif operate==3:
            pass
        elif operate==4:
            name = input("请输入你要删除的学生：")
            del_student(name.strip())
        elif operate==5:
            print_all_students()
        elif operate==6:
            print("退出成功！")
            break
        else:
            print("没有该选项，请重新输入")
