"""
    人为创造异常
        异常处理流程
        A -> B -> C -> D -> E
                        raise 异常类型(错误信息)
            try:
                ...
            except 异常类型 as 变量:
                变量.实例变量
"""


class Wife:
    def __init__(self, age=0):
        self.age = age  # 2

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 25 <= value <= 30:
            self.__age = value
        else:
            # 3
            # 快速传递错误消息
            # 扔出  异常对象
            raise Exception("我不要", 1001)


try:
    age = int(input("请输入年龄:"))
    w01 = Wife(age)  # 1
    print(w01.age)
# 接收
# except:
#     print("出错啦")
except Exception as e:
    print(e.args)
