"""
    运算符重载
        增强运算符
"""


class Vector2:
    """
        二维向量
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x轴{self.x},y轴{self.y}"

    # 算数运算符+ 返回新对象
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)

    # 累加运算符+= 返回自身对象
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

pos01 = Vector2(1, 2)
pos02 = Vector2(3, 4)
pos01 += pos02 # iadd --> add
print(pos01)


# 可变对象,在原有基础上变化  列表
# 不可变对象,产生新对象 元组
data01 = (1,)
print(id(data01))
data01 += (2,)
print(id(data01))
