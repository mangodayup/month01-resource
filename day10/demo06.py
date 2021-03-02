"""
    属性property
        原理:
           创建类变量,关联属性对象,覆盖实例变量
           属性对象需要读取和写入函数
        核心思想:
            拦截
"""


# 疑惑1:属性名等同于实例变量名
# 答:属性需要拦截类外对实例变量的操作

# 疑惑2:属性内部操作私有变量
# 答:私有变量实际存储数据,如果类外可以访问,那么失去保护作用.
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def get_age(self):  # 负责读取
        return self.__age

    def set_age(self, value):  # 负责写入
        self.__age = value

    # 创建类变量,关联属性,覆盖实例变量
    age = property(get_age, set_age)


shuang_er = Wife("双儿", 30)
print(shuang_er.name)
print(shuang_er.age)


class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 创建类变量,关联属性(读),覆盖实例变量
    @property  # age = property(读取函数)
    def age(self):  # 负责读取的函数
        return self.__age

    @age.setter  # age = age.setter(写入函数)
    def age(self, value):  # 负责写入的函数
        self.__age = value


shuang_er = Wife("双儿", 30)
print(shuang_er.name)
print(shuang_er.age)
