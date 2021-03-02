"""
    元组tuple - 基础操作
        创建
        定位(查找)
        遍历
"""
# 1. 创建
# 方式1:
tuple01 = (10, 20, 30)
# 方式2:
list01 = [43, 54, 65, 67]
tuple02 = tuple(list01)
print(tuple02)

# 2. 定位
print(tuple01[-1])
print(tuple01[:2])

# 3. 遍历
# 从头到尾读取
for item in tuple01:
    print(item)

# 非从头到尾读取
for i in range(len(tuple01) - 1, -1, -1):
    print(tuple01[i])

# 4. 创建元组时,在没有歧义情况下,括号可以省
tuple03 = 43, 5, 56, 76

# 5. 元组只有一个元素时,必须带逗号
tuple04 = (100,)
print(type(tuple04))

# 6.序列拆包
# 语法:  多个变量 = 一个容器
a, b, c = tuple01
a, b, c = "孙悟空"
a, b, c = [100, 200, 300]
# * 表示接收剩余的数据,结果为列表
a, *b = tuple01
print(a)
print(b)
print(c)
