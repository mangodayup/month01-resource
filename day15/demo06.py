"""
    迭代器
"""


class StudentController:
    def __init__(self):
        self.__list_student = []

    def add_student(self, stu):
        self.__list_student.append(stu)

    def __iter__(self):
        # 生成迭代器代码的大致规则:
        # 1. 将yield之前的代码存入__next__函数体
        # 2. 将yield之后的数据作为__next__返回值
        index = 0
        yield self.__list_student[index]

        index += 1
        yield self.__list_student[index]

        index += 1
        yield self.__list_student[index]


controller = StudentController()
controller.add_student("邱乾清")
controller.add_student("邹立朋")
controller.add_student("马晓宇")

iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
