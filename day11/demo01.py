"""
    封装设计思想
        分而治之 - 划分多个类
        变则疏之 - 寻找变化点
"""

# 需求:老张开车去东北
# 步骤:
# 1. 识别对象(行为不同用类区分)
#    人      车
# 2. 分配职责
#    使用    行驶
# 3. 建立交互
#    老张的使用方法调用车的行驶方法
# 方法1:直接创建对象
# 语义:老张每次去东北,都使用新车.
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def use(self,position):
        print(self.name,"去",position)
        car = Car()
        car.run()

class Car:
    def run(self):
        print("行驶")


# 数据不同用对象区分
lz = Person("老张")
ll = Person("老李")
lz.use("东北")
"""

# 方法2:在构造函数中创建对象
# 语义:老张开自己的车去东北
"""
class Person:
    def __init__(self, name=""):
        self.name = name
        self.car = Car()

    def use(self,position):
        print(self.name,"去",position)
        self.car.run()

class Car:
    def run(self):
        print("行驶")

lz = Person("老张")
lz.use("东北")
"""

# 方法3:定义类时不创建对象,通过参数传入
# 语义:老张使用交通工具去东北
class Person:
    def __init__(self, name=""):
        self.name = name

    def use(self, vehicle, position):
        print(self.name, "去", position)
        vehicle.run()


class Car:
    def run(self):
        print("行驶")


lz = Person("老张")
car = Car()
lz.use(car, "东北")
