"""
    字典推导式
        字典名 = {键:值 for 变量 in 可迭代对象 if 条件}
"""
# 需求：
# key:1-10之间的数字
# value:key的平方
# dict_result = {}
# for number in range(1, 11):
#     dict_result[number] = number ** 2
dict_result = {number: number ** 2 for number in range(1, 11)}
print(dict_result)

# 需求：
# key:1-10之间的奇数
# value:key的平方
# dict_result = {}
# for number in range(1, 11):
#     if number % 2:
#         dict_result[number] = number ** 2

dict_result = {
    number: number ** 2
    for number in range(1, 11)
    if number % 2
}
print(dict_result)
