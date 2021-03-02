"""
    三大编程范式
        面向过程编程:按部就班完成功能
            考虑问题从步骤出发,
            逐步细化，思考实现细节。
        面向对象编程:处理大的职责变化
            考虑问题从对象出发,
            谁负责干什么.
            封装、继承、多态
        函数式编程:处理小的功能变化
            分、  隔、  做
"""


# 笔试题：自定义排序算法
# 传统写法
# def sort(target):
#     for r in range(len(target) - 1):
#         for c in range(r + 1, len(target)):
#             if target[r] < target[c]:
#                 target[r], target[c] = target[c], target[r]
#
# list01 = [4, 5, 6, 6, 7, 8, 9, 0]
# sort(list01)
# print(list01)

# 函数式编程思想
#        数据灵活   行为灵活
def sort(target, condition):
    """
        对任意元素任意条件排序算法
    :param target:具有任意元素的列表
    :param condition:函数类型的条件
    """
    for r in range(len(target) - 1):
        for c in range(r + 1, len(target)):
            if condition(target[r], target[c]):
                target[r], target[c] = target[c], target[r]

list01 = [4, 5, 6, 6, 7, 8, 9, 0]
sort(list01, lambda a, b: a < b)
print(list01)

sort(list01, lambda a, b: a > b)
print(list01)
