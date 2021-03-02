"""
    创建颜色类Color,

"""


class Color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __gt__(self, other):
        return self.a > other.a


c01 = Color(150, 0, 0, 255)
c02 = Color(150, 0, 0, 255)
print(c01 == c02) # 根据__eq__判断,默认就比较地址,重写后可比较内容
print(c01 is c02) # 比较地址 False

list_colors = [
    Color(150, 0, 0, 255),
    Color(200, 0, 0, 255),
    Color(200, 0, 0, 255),
    Color(0, 200, 0, 255),
    Color(0, 0, 200, 255),
    Color(0, 0, 0, 255),
]
print(list_colors.count(Color(200, 0, 0, 255)))

print(max(list_colors))
list_colors.sort(reverse=True)
print(list_colors)