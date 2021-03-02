from typing import List
from model import StudentModel

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
