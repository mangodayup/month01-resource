"""
    lambda 应用
        作为实参
"""
from common.iterable_tools import IterableHelper

# def condition01(number):
#     return number % 2

list01 = [43, 45, 56, 6, 7]
# for item in IterableHelper.find_all(list01, condition01):
#     print(item)

for item in IterableHelper.find_all(list01, lambda number: number % 2):
    print(item)

# 在列表中查找所有小于10的数字
for item in IterableHelper.find_all(list01,lambda item:item < 10):
    print(item)
