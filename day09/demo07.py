"""
      现实世界         编程世界
     客观事物 -抽象-> 类 -具体-> 对象
"""


class Wife:
    def __init__(self, name, face_score, money):
        self.name = name
        self.face_score = face_score
        self.money = money

    def play(self):
        print(self.name, "在玩耍")


jian_ning = Wife("建宁", 95, 9999999)
jian_ning.money += 1
jian_ning.play()
