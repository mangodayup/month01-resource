"""
    列表推导式
        列表 = [对变量操作 for 变量 in 可迭代对象 if 条件]

"""
list01 = [9, 15, 65, 6, 78, 89]
# 需求:在list01中挑出能被3整除的数字存入list02
# list02 = []
# for item in list01:
#     if item % 3 == 0:
#         list02.append(item)
list02 = [item for item in list01 if item % 3 == 0]
print(list02)
# 需求:在list01中所有数字的个位存储list03
# list03 = []
# for item in list01:
#     list03.append(item % 10)
list03 = [item % 10 for item in list01]
print(list03)
