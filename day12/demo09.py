"""
    面向对象设计思想:
        封装(分):创建人类/飞机/汽车...
        继承(隔):创建交通工具隔离飞机/汽车...
        多态(做):通过重写实现飞机/汽车的具体功能
"""


# 老张开车去东北
# 增加:飞机/轮船...
# 缺点:违反开闭原则
# 允许增加新功能,拒绝客户端代码

class Person:
    def __init__(self, name=""):
        self.name = name

    def use(self, vehicle, position):
        if isinstance(vehicle, Vehicle):
            vehicle.transport()
            print("去", position)


class Vehicle:
    def transport(self):
        pass


class Car(Vehicle):
    def transport(self):
        print("行驶")


class Airplane(Vehicle):
    def transport(self):
        print("飞行")


lz = Person("老张")
lz.use(Car(), "东北")
lz.use(Airplane(), "东北")
lz.use("汽车", "东北")
