"""
    创建颜色类Color,
    包含红色r/绿色g/蓝色b/透明度a
    实现颜色对象的算数运算(至少两种).
"""


class Color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self):
        return str(self.__dict__)

    def __mul__(self, other):
        if type(other) == Color:
            r = self.r * other.r
            g = self.g * other.g
            b = self.b * other.b
            a = self.a * other.a
        else:
            r = self.r * other
            g = self.g * other
            b = self.b * other
            a = self.a * other
        return Color(r, g, b, a)


c01 = Color(150, 0, 0, 255)
c02 = Color(0, 200, 50, 255)
print(c01 * c02)
print(c01 * 2)
