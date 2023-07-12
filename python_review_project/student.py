'''
学生信息模块：
读取学生信息，保存学生信息
'''
class Student():
    # 学生信息变量
    def __init__(self) -> None:
        self.information=[]
        self.get_student_info()
    
    # 从txt中读取学生信息
    def get_student_info(self):   
        file=open('student_info.txt',encoding='utf-8')
        txt=file.read()
        lst=txt.split('\n')
        for w in lst:
            lst1=w.split( )
            self.information.append(lst1)
        self.information.pop(0)
        file.close()
    
    # 保存学生信息到txt文件
    def save_student_info(self):
        file=open('student_info.txt','w')
        file.write("name gender phone\n")
        for i in range(len(self.information)):
            if i!=len(self.information)-1:
                str=' '.join(self.information[i])+'\n'
            else:
                str=' '.join(self.information[i])
            file.write(str)
        file.close()



# S=Student()
# S.get_student_info()
# print(S.information)
# info=["joyce","f","227271616"]
# S.information.append(info)
# print(S.information)
# S.save_student_info()
