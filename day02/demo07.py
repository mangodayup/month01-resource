"""
    类型转换
        适用性:
            从终端中获得的数据类型都是str
            如果需要数学计算,必须类型转换
        语法:
            结果 = 目标类型(待转数据)

"""
#　结果 = 目标类型(待转数据)
# age = int(input("请输入年龄:"))
# print("明年:"+str(age + 1))

# str -> int
data01 = int("3")
# int -> str
data02 = str(5)

# str -> float
data03 = float("1.2")
# float -> str
data04 = str(1.2)

# int -> float
data05 = float(250)
# float -> int
data06 = int(1.9)
print(data06)  # 向下取整(截断删除)

# 注意：字符串转换为其他类型时,
# 必须是目标类型的字符串表达形式
# print(int("10.5"))　# 报错
# print(float("abc"))# 报错

