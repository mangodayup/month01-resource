"""
    继承 - 数据
"""
class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

"""
class Student(Person):
    pass


# 如果子类没有构造函数,直接使用父类构造函数.
stu01 = Student("悟空", 23)
"""

class Student(Person):
    # 子类构造函数参数:父类 + 子类
    def __init__(self, name="", age=0, score=0):
        super().__init__(name, age)
        self.score = score

# 如果子类有构造函数,覆盖父类构造函数.
# 内部一定通过super()调用父类构造函数
stu01 = Student("悟空", 23, 100)
print(stu01.name)
print(stu01.age)
print(stu01.score)
