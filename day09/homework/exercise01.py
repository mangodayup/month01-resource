"""
    定义函数,对数字列表进行升序排列
"""


def ascending(target):
    for r in range(len(target) - 1):        # 0     1   2
        for c in range(r + 1, len(target)):# 123   23   3
            if target[r] > target[c]:
                target[r], target[c] = target[c], target[r]

list01 = [170, 160, 180, 165]
ascending(list01)
print(list01)
