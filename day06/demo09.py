"""
    集合
        应用1：去重复
"""
# 1. 创建
# 方式1
# 语法：集合名 = {元素1,元素2}
set01 = {"悟空", "八戒", "唐僧"}
# 方式2
# 语法：集合名 = set(可迭代对象)
list01 = [5, 4, 5, 56, 5]
set02 = set(list01)

# 2. 添加
set01.add("小白龙")
set01.add("唐僧")

# 4. 遍历
for item in set01:
    print(item)

# 5. 删除
set01.remove("小白龙")
print(set01)