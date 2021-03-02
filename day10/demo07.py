"""
    属性各种写法
        读写属性
        只读属性
        *只写属性
"""


# 1. 读写属性:干预/控制对数据的读写过程
# 快捷键：props + 回车
class MyClass:
    def __init__(self, data=0):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


m01 = MyClass()
print(m01.data)


# 2. 只读属性:干预/控制对数据的读过程
#            拒绝写入(修改)
#    适用性:类中自行确定的数据,对外只希望读取,不希望修改.
# 快捷键：prop + 回车
class MyClass:
    def __init__(self):
        self.__data = 10

    @property
    def data(self):
        return self.__data


m01 = MyClass()
# m01.data = 10 # 不能修改
print(m01.data)


# 3. 只写属性:干预/控制对数据的写入过程
#            拒绝读取(访问)
# 快捷键：
class MyClass:
    def __init__(self, data=0):
        self.data = data

    data = property()

    @data.setter
    def data(self, value):
        self.__data = value


m01 = MyClass(10)
# print(m01.data) # 不能读取
print(m01.__dict__)
