"""
    迭代器
    # 需求:迭代自定义对象
"""


class StudentIterator:# 迭代器 __next__
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        if self.__index == len(self.__data) - 1:
            raise StopIteration()
        self.__index += 1
        return self.__data[self.__index]

class StudentController:# 可迭代对象__iter__
    def __init__(self):
        self.__list_student = []

    def add_student(self, stu):
        self.__list_student.append(stu)

    def __iter__(self):
        return StudentIterator(self.__list_student)

controller = StudentController()
controller.add_student("邱乾清")
controller.add_student("邹立朋")
controller.add_student("马晓宇")

# for item in controller:
#     print(item)
iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
