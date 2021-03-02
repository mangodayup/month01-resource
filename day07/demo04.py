"""
    函数
        价值：将制作与使用分离
"""
"""
# 制作(变化) + 使用
print("直拳")
print("摆拳")
print("勾拳")
print("闪电鞭")
print("乾坤大挪移")
# ....
# 制作(变化) + 使用
print("直拳")
print("摆拳")
print("勾拳")
print("闪电鞭")
print("乾坤大挪移")
"""


# 制作(变化)
def attack():
    print("直拳")
    print("摆拳")
    print("勾拳")
    print("闪电鞭")
    print("乾坤大挪移")
    print("降龙十八掌")


# 使用
attack()  # 如果需要调试时进入函数体,按F7
attack()
attack()
