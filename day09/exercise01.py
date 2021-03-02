"""
    练习:定义函数,数值累乘
"""


def multiplicative(*args):
    result = 1
    for item in args:
        result *= item
    return result

# 调用者无需构建容器,传入多个数据
print(multiplicative(4, 354, 5, 67, 7))


# def multiplicative(target):
#     result = 1
#     for item in target:
#         result *= item
#     return result
#
#
# print(multiplicative([4, 354, 5, 67, 7]))
