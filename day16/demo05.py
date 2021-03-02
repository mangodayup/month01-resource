"""
    函数式编程思想
        适用性：
            多个函数,主体部分相同,核心算法不同.
        特征：
            "封装"分：将变化点和主体部分单独定义到函数中
            "继承"隔：使用参数抽象变化点,先确定调用方法，从而实现了隔离变化
            "多态"做：增加新功能,就创建新函数实现具体功能,最后调用通用函数.
"""
list01 = [43, 4, 5, 56, 76, 78, 8]


# 需求1：定义函数,查找列表所有偶数
def find01():
    for item in list01:
        if item % 2 == 0:
            yield item


# 需求2：定义函数,查找列表所有大于10的数字
def find02():
    for item in list01:
        if item > 10:
            yield item


# for number in find02():
#     print(number)

# 分：
def condition01(item):
    return item % 2 == 0


def condition02(item):
    return item > 10


def find(condition):  # 抽象
    for item in list01:
        # if item % 2 == 0:
        # if condition01(item):
        # if condition02(item):
        if condition(item):  # 统一
            yield item


# 增加新需求：查找小于50的数
def condition03(item):
    return item < 50


for item in find(condition03):
    print(item)
