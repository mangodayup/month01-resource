"""
    zip
        取出多个可迭代对象中对应的元素形成元组
"""
list01 = ["张无忌", "赵敏", "周芷若"]
list02 = [1001, 1002, 1003]
for item in zip(list01, list02):
    print(item)

map = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
# 矩阵转置
# new_map = []
# for item in zip(map[0], map[1],map[2], map[3]):
#     new_map.append(list(item))

# new_map = [list(item) for item in zip(map[0], map[1], map[2], map[3])]

new_map = [list(item)
           for item in zip(*map)]
print(new_map)
