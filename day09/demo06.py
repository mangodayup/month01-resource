"""
    自学容器函数
"""
list01 = [4,7,54,6,78,6]
# 在列表中查找元素索引
# 如果不存在则报错
if 100 in list01:
    print(list01.index(100))

# 在列表中查找元素数量
print(list01.count(100))

# 删除索引对应的元素，如果不加索引，默认删除最后元素，同时返回删除元素的引用关系
print(list01.pop(0)) # 4
print(list01.pop()) # 6
print(list01) # [7, 54, 6, 78]
# 一次追加多个元素
list01.extend([10,20])

# 升序排列
list01.sort()
# 降序排列
list01.sort(reverse = True)
print(list01)