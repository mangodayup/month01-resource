"""
    练习5:
       玩家攻击敌人,敌人受伤(减少血量,掉落装备).
       敌人攻击玩家,玩家受伤(减少血量,闪现红屏).
"""


class Player:
    def __init__(self, hp=0, atk=0):
        self.hp = hp
        self.atk = atk

    # 完全相同
    def attack(self, target):
        print("攻击")
        target.damage(self.atk)

    # 部分相同
    def damage(self, value):
        self.hp -= value
        print("受伤,血量:", self.hp)
        print("闪现红屏")


class Enemy:
    def __init__(self, hp=0, atk=0):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        self.hp -= value
        print("受伤,血量:", self.hp)
        print("掉落装备")

    def attack(self, target):
        print("攻击")
        target.damage(self.atk)


p01 = Player(500, 50)
e01 = Enemy(100, 30)
p01.attack(e01)
e01.attack(p01)
