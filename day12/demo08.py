"""
    面向对象设计思想:
        封装
        继承
        多态
"""


# 老张开车去东北
# 增加:飞机/轮船...
# 缺点:违反开闭原则
# 允许增加新功能,拒绝客户端代码

class Person:
    def __init__(self, name=""):
        self.name = name

    def use(self, vehicle, position):
        print("去", position)
        if type(vehicle) == Car:
            vehicle.run()
        elif type(vehicle) == Airplane:
            vehicle.fly()


class Car:
    def run(self):
        print("行驶")


class Airplane:
    def fly(self):
        print("飞行")


lz = Person("老张")
lz.use(Car(), "东北")
lz.use(Airplane(), "东北")
