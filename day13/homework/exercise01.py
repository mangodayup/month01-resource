"""
    小明使用手机打电话
    要求:增加座机,卫星电话时不影响小明.
    封装[分]：根据行为不同,划分类,[识别变化]
        创建人类和手机类
    继承[隔]：让不同类型在一个行为上达到统一
        使用通信工具类,隔离人类与手机、座机等具体工具的变化
    多态[做]：框架先确定用法,实现类后完成做法.
        通过重写实现手机的功能

    开闭原则：增加新通信工具,人类不变.
    单一职责:
        人类负责打电话.
        手机/座机实现相应的通话功能
    依赖倒置:人类调用通信工具,不调用手机/座机
    组合复用:
        人类使用组合关系连接通话算法
        没有通过继承调用通话算法.
    里氏替换:
        人类打电话方法,形参是通信工具,实参是手机/座机
        手机/座机在重写时,先通过super()调用员工方法,再定义新算法.
        扩展重写:先通过super()调用父类方法
                再增加新功能
    迪米特法则:
        人类与手机/座机是低耦合关系
"""

class Person:
    def __init__(self, name=""):
        self.name = name

    def call(self,communication):
        print(self.name, "打电话")
        # 1. 编码时  [调用父]
        #    运行时  执行子
        communication.dialing()

class Communication:
    def dialing(self):
        pass

class MobilePhone(Communication):
    # 2. [子重写] 体现个性(实现变化)
    def dialing(self):
        super().dialing()
        print("手机呼叫")

class Landline(Communication):
    def dialing(self):
        super().dialing()
        print("座机呼叫")

xm = Person("小明")
# 3. [创建子]对象
xm.call(MobilePhone())
xm.call(Landline())
