"""
    创建颜色类Color,
    包含红色r/绿色g/蓝色b/透明度a
    实现颜色对象的增强运算符运算(至少两种).
"""


class Color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self):
        return str(self.__dict__)

    def __ipow__(self, other):
        self.r **= other
        self.g **= other
        self.b **= other
        self.a **= other
        return self


c01 = Color(150, 0, 0, 255)
c01 **= 2
print(c01)
