"""
    类成员
        类变量
            创建
                在类中,方法外:
                    类变量名 = 数据
            使用
                通过类名
        类方法
            价值
                操作类变量

"""


class ICBC:
    # 类变量:不同对象相同数据  ［大家的］
    total_money = 1000000

    # 类方法:操作类变量
    @classmethod
    def print_total_money(cls):
        print("总行的钱:", cls.total_money)

    def __init__(self, name="", money=0):
        # 实例变量:不同对象不同数据　　［自己的］
        self.name = name
        self.money = money
        # 创建支行时,总行的钱减少了
        ICBC.total_money -= money


tian_tian = ICBC("天坛支行", 100000)
# print(ICBC.total_money)
ICBC.print_total_money()

xi_dan = ICBC("西单支行", 200000)
# print(ICBC.total_money)
ICBC.print_total_money()

# 天坛支行钱变动，不影响西单支行
tian_tian.money += 10000
print(xi_dan.money)
