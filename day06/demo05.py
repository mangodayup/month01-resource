"""
    字典基础操作
        创建
"""
# 1. 创建字典
# 方式1:字典名 = {键1:值1,键2:值2}
dict_person_gb = {
    "name": "高博",
    "age": 26,
    "sex": "女"
}
dict_person_jth = {
    "name": "纪添皓",
    "age": 25,
    "sex": "男"
}
# 方式2:字典名 = dict(可迭代对象)
# 可迭代对象格式要求:元素能够一分二
list01 = ["唐僧", ("猪", "八戒"), ["沙", "僧"]]
dict_data = dict(list01)
print(dict_data)