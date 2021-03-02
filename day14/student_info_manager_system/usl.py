from bll import StudentController
from model import StudentModel


class StudentView:
    """
        界面视图:负责界面逻辑,输入/输出..
    """

    def __init__(self):
        self.__controller = StudentController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_item()

    def __display_menu(self):
        print("按1键录入学生信息")
        print("按2键显示学生信息")
        print("按3键删除学生信息")
        print("按4键修改学生信息")

    def __select_item(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__display_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名:")
        stu.age = int(input("请输入学生年龄:"))
        stu.score = int(input("请输入学生成绩:"))
        self.__controller.add_student(stu)

    def __display_students(self):
        for item in self.__controller.list_students:
            print(f"{item.name}的编号是{item.sid},年龄是{item.age},成绩是{item.score}")

    def __delete_student(self):
        sid = int(input("请输入学生编号:"))
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        stu.sid = int(input("请输入学生编号:"))
        stu.name = int(input("请输入学生姓名:"))
        stu.age = int(input("请输入学生年龄:"))
        stu.score = int(input("请输入学生成绩:"))
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")