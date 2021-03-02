"""
    返回值
        制作函数时给使用函数时传递的信息
"""


# 需求：两个数值相加的函数
# 缺点：一个函数做了3个功能（输入 计算 输出）
# def add():
#     one = int(input("请输入第一个数字："))
#     two = int(input("请输入第二个数字："))
#     result = one + two
#     print("结果是：%d" % result)
#
# add()


def add(one, two):
    result = one + two
    # 返回 数据
    return result


res = add(5, 3)
print(res)
