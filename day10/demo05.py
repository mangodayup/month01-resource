"""
    属性property
        作用:
            保障数据在有效范围内
"""


# 疑惑1:属性名等同于实例变量名
# 疑惑2:属性内部操作私有变量
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age  # self.age(30)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 22 <= value <= 30:
            self.__age = value
        else:
            # 创造错误
            raise Exception("我不娶")


shuang_er = Wife("双儿", 30)
print(shuang_er.name)
print(shuang_er.age)  # shuang_er.age()
