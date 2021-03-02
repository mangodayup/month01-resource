"""
    字典基础操作
        添加
        定位
"""
dict_person = {
    "name": "高博",
    "age": 26,
    "sex": "女"
}
# 1. 添加
# 语法：字典名[键] = 值
if "money" not in dict_person:
    dict_person["money"] = 9999999
# 2. 定位
# 语法：字典名[键]
# --修改
if "name" in dict_person:
    dict_person["name"] = "老高"
# -- 读取
print(dict_person["age"])
#     练习2：
#         在终端中打印香港的现有人数
#         在终端中打印上海的新增和现有人数
#         新疆新增人数增加1