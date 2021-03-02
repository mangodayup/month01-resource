"""
   玩家攻击敌人,敌人受伤(减少血量,掉落装备).
   敌人攻击玩家,玩家受伤(减少血量,闪现红屏).
"""

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
        if self.hp <= 0:
            self.death()

    # 完全不同
    def death(self):
        print("游戏结束")


class Enemy:
    def __init__(self, hp=0, atk=0):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        self.hp -= value
        print("受伤,血量:", self.hp)
        print("掉落装备")
        if self.hp <= 0:
            self.death()

    def attack(self, target):
        print("攻击")
        target.damage(self.atk)

    def death(self):
        print("加分")


p01 = Player(500, 50)
e01 = Enemy(100, 30)
p01.attack(e01)
e01.attack(p01)
"""


class Character:
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
        if self.hp <= 0:
            self.death()

    # 完全不同
    def death(self):
        pass


class Player(Character):
    # 部分相同
    def damage(self, value):
        print("闪现红屏")
        super().damage(value)

    # 完全不同
    def death(self):
        print("游戏结束")


class Enemy(Character):

    def damage(self, value):
        print("掉落装备")
        super().damage(value)

    def death(self):
        print("加分")


p01 = Player(500, 50)
e01 = Enemy(100, 30)
p01.attack(e01)
e01.attack(p01)
p01.attack(e01)

