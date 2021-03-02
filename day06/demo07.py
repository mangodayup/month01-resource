"""
    字典基础操作
        删除
        遍历
"""
dict_person = {
    "name": "高博",
    "age": 26,
    "sex": "女"
}
# 1. 删除
# 语法：del 字典名[键]
# del dict_person["sex"]
# print(dict_person)

# 2. 遍历
# -- 所有key
for key in dict_person:
    print(key)
# -- 所有value
for value in dict_person.values():
    print(value)
# -- 所有key value
# item 得到的是元组 (key,value)
# for item in dict_person.items():
#     print(item[0])
#     print(item[1])
for k, v in dict_person.items():
    print(k)
    print(v)

# ['name', 'age', 'sex']
print(list(dict_person))
# ['高博', 26, '女']
print(list(dict_person.values()))
# [('name', '高博'), ('age', 26), ('sex', '女')]
print(list(dict_person.items()))
