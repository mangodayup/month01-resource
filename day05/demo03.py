"""
    列表 list
        创建
        添加
"""
# 1. 创建列表
# 语法1:
#   列表名 = [元素1, 元素2]
# 姓名列表
list_name = ["纪添皓", "沙忠金", "熊志鹏"]
# 年龄列表
list_age = [35, 22, 28]

# 语法2:
#   列表名 = list(可迭代对象)
list01 = list("孙悟空")
print(list01)

# 2. 添加元素
# -- 追加:列表名.append(元素)
list_name.append("刘柄曈")
# -- 插入 陈浩明
list_name.insert(2, "陈浩明")
