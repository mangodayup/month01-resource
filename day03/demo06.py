"""
    if elif
    调试
        定义:
            让程序中断,逐语句执行;
            审查程序执行过程和变量取值.
        步骤:
            1. 加断点(在可能出错的行)
            2. 开始调试(Debug)
            3. 逐语句执行(F8)
"""
num = float(input("请输入数字:"))
# 缺点:所有条件都需要判断
# if num > 0:
#     print("正数")
# if num < 0:
#     print("负数")
# if num == 0:
#     print("零")

# else 属于上面的if
if num > 0:
    print("正数")
elif num < 0:  # 上面条件满足,本行条件不判断
    print("负数")
else:
    print("零")
