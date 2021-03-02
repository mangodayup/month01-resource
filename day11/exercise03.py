"""
    练习4：以面向对象思想,描述下列情景.
        玩家攻击敌人,敌人受伤(根据玩家攻击力，减少敌人的血量).

    练习5:
       玩家攻击敌人,敌人受伤(减少血量,掉落装备).
       敌人攻击玩家,玩家受伤(减少血量,闪现红屏).
"""
class Player:
    def __init__(self, atk=0):
        self.atk = atk

    def attack(self,target):
        print("攻击")
        target.damage(self.atk)

class Enemy:
    def __init__(self, hp=0):
        self.hp = hp

    def damage(self,value):
        self.hp -= value
        print("受伤,血量:",self.hp)

p01 = Player(50)
e01 = Enemy(100)
p01.attack(e01)
p01.attack(e01)
