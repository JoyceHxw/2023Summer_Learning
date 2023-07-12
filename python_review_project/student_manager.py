from student import Student

'''
管理系统模块：
对学生信息进行操作
'''
class System():
    # 获取学生信息
    def __init__(self) -> None:
        self.students=Student()
        self.information=self.students.information

    # 展示功能模块
    def show(self):
        function="----------------------------------\n1.添加学生\n2.删除学生\n3.修改学生信息\n4.查询学生信息\n5.显示所有学生信息\n6.保存修改\n7.退出系统\n请选择功能前的序号："
        print(function)

    # 添加学生
    def add_student(self):
        info=[]
        print("请输入学生姓名：")
        name=input()
        info.append(name)
        while True:
            print("请输入学生性别（f/m）：")
            gender=input()
            if gender=='f' or gender=='m':
                info.append(gender)
                break
            else:
                print("输入格式错误，请重新输入")
        while True:
            print("请输入学生手机号：")
            phone=input()
            if phone.isdigit():
                info.append(phone)
                break
            else:
                print("输入格式错误，请重新输入")
        self.information.append(info)
        print("添加成功")
    
    # 删除学生
    def del_student(self):
        print("请输入要删除的学生的编号：")
        num=input()
        if num.isdigit():
            num=int(num)
        else:
            print("输入格式错误，退出该功能！")
            return
        if num<=0 or num>len(self.information):
            print("删除失败！该学生不存在")
        else:
            self.information.pop(num-1)
            print("删除成功！")
    
    # 修改学生信息
    def modify_info(self):
        print("请输入要修改信息的学生的编号：")
        num=input()
        if num.isdigit():
            num=int(num)
        else:
            print("输入格式错误，退出该功能！")
            return
        if num<=0 or num>len(self.information):
            print("修改失败！该学生不存在")
        else:
            print("请选择要修改的信息（n：姓名/g：性别/p：手机号）：")
            mod_choice=input()
            if mod_choice=='n':
                print("请输入新的姓名：")
                new_name=input()
                self.information[num-1][0]=new_name
                print("修改成功！")
            elif mod_choice=='g':
                while True:
                    print("请输入新的性别：")
                    new_gender=input()
                    if new_gender=='f' or new_gender=='m':
                        self.information[num-1][1]=new_gender
                        break
                    else:
                        print("输入格式错误，请重新输入")
                print("修改成功！")
            elif mod_choice=='p':
                while True:
                    print("请输入新的手机号：")
                    new_phone=input()
                    if new_phone.isdigit():
                        self.information[num-1][2]=new_phone
                        break
                    else:
                        print("输入格式错误，请重新输入")
                print("修改成功！")
            else:
                print("修改失败！输入格式错误")
    
    # 查询学生信息
    def find_student(self):
        print("请输入要查询的学生的编号：")
        num=input()
        if num.isdigit():
            num=int(num)
        else:
            print("输入格式错误，退出该功能！")
            return
        if num<=0 or num>len(self.information):
            print("查询失败！该学生不存在")
        else:
            str1="NO.".ljust(5)+"NAME".ljust(10)+"GENDER".ljust(10)+"PHONE".ljust(15)
            str2=f"{num}".ljust(5)+f"{self.information[num-1][0]}".ljust(10)+f"{self.information[num-1][1]}".ljust(10)+f"{self.information[num-1][2]}".ljust(15)
            print(str1)
            print(str2)
    
    # 显示所有学生信息
    def show_all(self):
        str1="NO.".ljust(5)+"NAME".ljust(10)+"GENDER".ljust(10)+"PHONE".ljust(15)
        print(str1)
        str=""
        for i,info in enumerate(self.information):
            str+=f"{i+1}".ljust(5)+f"{info[0]}".ljust(10)+f"{info[1]}".ljust(10)+f"{info[2]}".ljust(15)+'\n'
        print(str)
    
    # 保存修改
    def save(self):
        self.students.save_student_info()
        print("保存成功！")

    # 系统运行
    def run(self):
        print("欢迎进入学生信息管理系统！")
        while True:
            self.show()
            num=input()
            if num=='1':
                self.add_student()
            elif num=='2':
                self.del_student()
            elif num=='3':
                self.modify_info()
            elif num=='4':
                self.find_student()
            elif num=='5':
                self.show_all()
            elif num=='6':
                self.save()
            elif num=='7':
                while True:
                    print("是否保存修改？（y/n）：")
                    c=input()
                    if c=='y':
                        self.save()
                        print("成功退出系统！")
                        return
                    elif c=='n':
                        print("成功退出系统！")
                        return
                    else:
                        print("输入错误，请重新输入")
                        
            else:
                print("请重新输入：")
# S=System()
# S.run()
        