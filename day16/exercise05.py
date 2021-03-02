"""
    练习：
    将find_all封装到common/iterable_tools的
    的IterableHelper类中作为静态方法
    实现下列效果：
    在列表中查找所有字符串
    在列表中查找所有大于20的数字
"""
from common.iterable_tools import IterableHelper


# 参数是列表的每个元素
# 返回值是查找的条件
def condition01(item):
    return type(item) == str


def condition02(item):
    return type(item) in (int, float) and item > 20


list01 = [43, 45, "56", 67, "78", 9]

for item in IterableHelper.find_all(list01, condition01):
    print(item)

for item in IterableHelper.find_all(list01, condition02):
    print(item)
