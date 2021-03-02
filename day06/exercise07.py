dict_HongKong = {
    "region": "香港",
    "new": 15,
    "now": 393,
    "total": 4801,
    "cure": 4320,
    "death": 88
}

dict_shanghai = {
    "region": "上海",
    "new": 6,
    "now": 61,
    "total": 903,
    "cure": 835,
    "death": 7
}

dict_xingjiang = {
    "region": "新疆",
    "new": 0,
    "now": 49,
    "total": 902,
    "cure": 850,
    "death": 3
}

# 练习3：
#  删除香港现有人数信息
#  删除新疆新增人数信息
#  删除上海的新增和现有信息
del dict_HongKong["now"]
del dict_xingjiang["new"]
del dict_shanghai["new"], dict_shanghai["now"]

for key in dict_HongKong:
    print(key)

for value in dict_shanghai.values():
    print(value)

for key, value in dict_xingjiang.items():
    print(key)
    print(value)

for key, value in dict_shanghai.items():
    if value == 61:
        print(key)
        break
