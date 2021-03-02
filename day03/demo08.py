"""
    条件表达式
        适用性:根据条件为变量赋值
        语法:
            变量=满足条件的值 if 条件 else 不满足条件的值
"""
if input("请输入性别:") == "男":
    value = 1
else:
    value = 0

value = 1 if input("请输入性别:") == "男" else 0
