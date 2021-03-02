"""
    生成器表达式
        将列表推导式的[]替换为()即可


        生成器表达式优点:
            节省内存
        生成器表达式缺点:
            只能使用一次
            读取数据不灵活(不支持索引切片)
        列表推导式优点:
            可以反复使用
            操作数据灵活
        列表推导式缺点:
            比较占内存
"""

list01 = [9, 15, 65, 6, 78, 89]
# 需求:在list01中挑出能被3整除的数字存入list02
# list02 = [item for item in list01 if item % 3 == 0]
#
# for item in list02:
#     print(item)

generator02 = (item for item in list01 if item % 3 == 0)

for item in generator02:
    print(item)

for item in generator02:
    print(item)

# 需求:在list01中所有数字的个位存储list03
list03 = [item % 10 for item in list01]
generator03 = (item % 10 for item in list01)
# for item in list03:
#     print(item)
for item in generator03:
    print(item)

