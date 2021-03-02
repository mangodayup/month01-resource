"""

"""


class Grenade:
    # 星号元组形参
    def explode(self, *targets):
        print("爆炸")
        for item in targets:
            if isinstance(item, AttackTarget):
                item.damage()


class AttackTarget:
    def damage(self):
        pass


class Player(AttackTarget):
    def damage(self):
        print("碎屏")


class Enemy(AttackTarget):
    def damage(self):
        print("头顶爆字")


g01 = Grenade()
g01.explode(Player(), Enemy())
g01.explode("玩家")
