"""
练习：
    在终端中输入一个四位整数，
    计算每位相加和。
    例如：
        录入1234，打印1+2+3+4结果
    效果：
        请输入四位整数：1234
        结果是：10
    提示：
        整数与10取余数,可以获得个位
"""
number = int(input("请输入四位整数："))
# 写法1:算数运算符
# 个位
unit01 = number % 10
# 十位
# 1234 //10 --> 123 % 10 -->3
unit02 = number // 10 % 10
# 百位
# 1234 //100 --> 12 % 10 -->2
unit03 = number // 100 % 10
# 千位
# 1234 //1000 --> 1
unit04 = number // 1000
result = unit01 + unit02 + unit03 + unit04
print(result)

# 写法2:算数运算符
number = 1234
result = number % 10
result += number // 10 % 10
result += number // 100 % 10
result += number // 1000
