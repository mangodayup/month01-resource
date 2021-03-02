"""
    Python语言设计理念
         简洁自由,去除变量的类型.
        优点:
            简单,适合数学计算
        缺点:
            不适合大型软件开发
            变量没有类型,意味着不知道变量对应的操作

        解决方案:
            Python类型标注
                语法:
                    变量名:类型     普通变量/参数
                    # type:类型    实例变量
                    -> 类型        返回值
                作用:
                    增强代码可读性
                    类型检查
"""
# 准备列表标注工具
from typing import List


class StudentModel:
    """
        学生模型:封装数据
    """

    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name  # type:str
        self.age = age  # type:int
        self.score = score  # type:int
        # 唯一标识数据的编号
        self.sid = sid  # type:int


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


class StudentController:
    """
        学生控制器:负责业务逻辑
    """
    __start_id = 1001

    @classmethod
    def __set_sid(cls, stu: StudentModel):
        stu.sid = cls.__start_id
        cls.__start_id += 1

    def __init__(self):
        self.__list_students = []  # type:List[StudentModel]

    @property  # 只读属性
    def list_students(self):
        return self.__list_students

    def add_student(self, stu: StudentModel):
        """
            添加学生信息
        :param stu: 需要添加的学生对象
        """
        # StudentController.__set_sid(stu)
        self.__list_students.append(stu)

    def remove_student(self, sid: int) -> bool:
        """
            移除学生
        :param sid:学生编号
        :return: 是否移除成功
        """
        for i in range(len(self.__list_students)):
            if self.__list_students[i].sid == sid:
                del self.__list_students[i]
                return True
        return False

    def update_student(self, stu: StudentModel) -> bool:
        """
            更新学生信息
        :param stu: 需要更新的学生信息
        :return: 是否更新成功
        """
        # for i in range(len(self.__list_students)):
        #     if self.__list_students[i].sid == stu.sid:
        #         self.__list_students[i].__dict__ = stu.__dict__
        for item in self.__list_students:
            if item.sid == stu.sid:
                item.__dict__ = stu.__dict__
                return True
        return False


view = StudentView()
view.main()
