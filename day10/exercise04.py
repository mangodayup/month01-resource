"""
    练习:创建技能类
    数据：技能名称,冷却时间,攻击力度,消耗法力
               0--120   0--200   0--100
        读写属性:冷却时间 攻击力度
        只读属性:消耗法力
"""


class Skill:
    def __init__(self, name="", duration=0, atk=0):
        self.name = name
        self.duration = duration
        self.atk = atk
        self.__cost_sp = 60

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if 0 <= value <= 120:
            self.__duration = value
        else:
            raise Exception("冷却时间超过范围")

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if value < 0:
            value = 0
        if value > 200:
            value = 200
        self.__atk = value

    @property
    def cost_sp(self):
        return self.__cost_sp


xlsbz = Skill("降龙十八掌", 60, 50)
print(xlsbz.name)
print(xlsbz.duration)
print(xlsbz.cost_sp)
print(xlsbz.atk)
