"""
    内置生成器
        enumerate 根据元素生成对应的索引
        可以通过元素判断数据
              索引修改数据
        又几乎不占用内存
"""
list01 = [4, 54, 5, 16, 8]
# 从头到尾读取
# 快捷键：iter + 回车
for item in list01:
    print(item)

# 非从头到尾读取
for i in range(len(list01)):
    print(list01[i])

# 从头到尾操作数据
# 快捷键：itere + 回车
# item 存储的是(索引,元素)
# for item in enumerate(list01):
#     print(item)
for i, item in enumerate(list01):
    if item > 10:
        list01[i] = 0

dict01 = {"a": "A", "b": "B"}
for i, key in enumerate(dict01):
    print(i, key)

for i, (key, value) in enumerate(dict01.items()):
    print(i, key, value)
