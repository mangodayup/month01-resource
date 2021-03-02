"""
    创建图形管理器
	1. 记录多种图形（圆形、矩形....）
	2. 提供计算总面积的方法.
    满足：
        开闭原则
    测试：
        创建图形管理器，存储多个图形对象。
        通过图形管理器，调用计算总面积方法.
    写出三大特征的具体体现
        封装:创建图形管理器/圆形/矩形
        继承:创建图形类隔离图形管理器与圆形/矩形的变化
        多态:圆形/矩形重写图形类的计算面积方法实现具体功能

    写出图形管理器设计原则的具体体现
        开闭原则：增加新图形,图形管理器不变.
        单一职责:
            图形管理器负责统一管理所有图形,获取总面积.
            圆形员类负责圆形的面积算法
            矩形员类负责矩形的薪资算法
        依赖倒置:图形管理器调用图形类,不调用圆形/矩形.
        组合复用:
            图形管理器使用组合关系连接图形面积算法
            没有通过继承调用图形薪资算法.
        里氏替换:
            图形管理器添加图形方法,形参是图形,实参是圆形/矩形
            圆形/矩形在重写时,先通过super()调用员工方法,再定义新算法.
            扩展重写:先通过super()调用父类方法
                    再增加新功能
        迪米特法则:
            图形管理器与圆形/矩形是低耦合关系
"""
from typing import List

class GraphicController:
    def __init__(self):
        self.__all_graphice = [] # type:List[Graphic]

    def add_graphice(self, graphice):
        self.__all_graphice.append(graphice)

    def get_total_area(self):
        total_area = 0
        for item in self.__all_graphice:
            # 先用
            # 1. 编码时 调用父
            #    运行时 执行子
            total_area += item.calculate_area()
        return total_area


class Graphic:
    def calculate_area(self):
        return 0


class Circle(Graphic):
    def __init__(self, r):
        self.r = r

    # 后做
    # 2. 子重写
    def calculate_area(self):
        return super().calculate_area()+3.14 * self.r ** 2


class Rectanle(Graphic):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def calculate_area(self):
        return super().calculate_area()+self.l * self.w


controller = GraphicController()
# 3. 创建子
controller.add_graphice(Circle(5))
controller.add_graphice(Rectanle(2, 7))
print(controller.get_total_area())