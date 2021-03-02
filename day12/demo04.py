"""

"""


class Person(object):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 改变行为
    # 爸爸的__str__,在返回对象内存地址
    # 子类的__str__,在返回自定义格式
    def __str__(self):
        return f"我是{self.name},今年{self.age}岁了"

wk = Person("悟空",23)
print(wk)