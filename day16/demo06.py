"""

"""
from common.iterable_tools import IterableHelper


def condition01(item):
    return item % 2 == 0

def condition02(item):
    return item > 10

def condition03(item):
    return item < 50

list01 = [43, 4, 5, 56, 76, 78, 8]
# 查找所有偶数
# 惰性操作 - 节省内存
for item in IterableHelper.find_all(list01,condition01):
    print(item)

# 立即操作 - 操作灵活
result = list(IterableHelper.find_all(list01,condition01))
print(result[0])
print(result[-1])
print(result[-3:])



