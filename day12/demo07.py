"""
    运算符重载
        比较运算符
        自定义对象容器,需要使用内置函数,必须重写__eq__
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x轴{self.x},y轴{self.y}"

    # 决定了两个对象是否相同的依据
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # 决定了两个对象比较大小的依据
    def __lt__(self, other):
        return self.x ** 2 + self.y ** 2 < other.x ** 2 + other.y ** 2


pos01 = Vector2(1, 1)
list_vector = [
    Vector2(1, 1),
    Vector2(3, 3),
    Vector2(2, 2),
    Vector2(5, 5),
    Vector2(4, 4),
]
pos02 = Vector2(1, 1)
print(pos01 == pos02)  #

print(Vector2(3, 3) in list_vector)
#
# list_vector.count()
# list_vector.index()

# 自定义类型不具备__lt__
print(min(list_vector))
list_vector.sort()
print(list_vector)
