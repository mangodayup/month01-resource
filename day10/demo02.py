"""
    小结-Python语言变量
"""
# 全局变量:整个文件可用
data01 = 10

def func01():
    # 局部变量:一个函数可用
    data02 = 20

class MyClass:
    # 类变量:通过类名调用
    data04 = 40
    def __init__(self):
        # 实例变量:通过对象调用
        self.data03 = 30

m01 = MyClass()
print(m01.data03)
print(MyClass.data04)