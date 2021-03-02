"""
    私有成员
        语法:以双下划线命名
        作用:类外无法使用
        原理:障眼法-看见的和实际的不同
                 __data    _MyClass__data
                 私有名称   _+类名+私有名称
"""
class MyClass:
    def __init__(self, data=""):
        self.__data = data

    def __func01(self):
        print("func01执行了")

    def func02(self):
        print(self.__data)
        self.__func01()

m01 = MyClass("参数")
# print(m01.__data)
# m01.__func01()
# m01.func02()
# print(m01._MyClass__data)
# m01._MyClass__func01()
print(m01.__dict__)