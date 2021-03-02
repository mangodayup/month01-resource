"""
    函数
        参数:本质就是变量
           制作功能时要求使用功能时提供的信息

"""


# 形式参数：表面的不具体的数据
def attack(count):
    for __ in range(count):
        print("直拳")
        print("摆拳")
        print("勾拳")


# 实际参数：真实的具体的数据
attack(5)
attack(2)
