"""
    创建敌人类,保障敌人血量在1-100之间
    如果超过范围,
    传递错误消息(错误原因,错误编号).
"""
class Enemy:
    def __init__(self, hp=0):
        self.hp = hp

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0<= value <=100:
            self.__hp = value
        else:
            raise Exception("血量超过范围",1001)

try:
    hp = int(input("请输入血量:"))
    e01 = Enemy(hp)
    print(e01.hp)
except Exception as e:
    print(e.args)