"""
    练习1：
    需求：
        定义函数，在列表中查找奇数
        定义函数，在列表中查找能被3或5整除的数字
    步骤：
        1. 根据需求，写出函数。
        2. 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数find_all
        3. 在当前模块中调用
"""
list01 = [4, 5, 45, 6, 7, 89]


# 缺点：多个函数主体部分重复
def find_all01():
    for item in list01:
        if item % 2:
            yield item


def find_all02():
    for item in list01:
        if item % 3 == 0 or item % 5 == 0:
            yield item


# 1.分-变化
def condition01(element):
    return element % 2


def condition02(item):
    return item % 3 == 0 or item % 5 == 0


# 1.分-通用
def find_all(condition):  # 2. 隔-参数
    for item in list01:
        # if item % 2:
        # if condition01(item):
        # if condition02(item):
        if condition(item):
            yield item


# 3. 做-新功能
def condition03(item):
    return item < 10


for item in find_all(condition03):
    print(item)
