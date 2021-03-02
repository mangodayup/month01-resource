"""
    建议:通过对象访问实例成员
        通过类访问类成员
    也可以但是不建议:
      交叉访问(通过对象访问类成员,通过类访问实例成员)
"""

class MyClass:
    # 自动传递对象
    def func01(self):
        print("实例方法")

    @classmethod # 自动传递类
    def func02(cls):
        print("类方法")


# 建议
m01 = MyClass()
m01.func01()
MyClass.func02()

# 不建议
m01.func02()  # 通过对象访问类方法
MyClass.func01(m01)  # 通过类访问实例方法
