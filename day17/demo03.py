"""
    内置高阶函数
"""

class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money


# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空2", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

# map 映射:
# select
for name in map(lambda item:item.name,list_employees):
    print(name)

# filter 过滤器：
# find_all
for emp in filter(lambda item:item.money > 20000,list_employees):
    print(emp.__dict__)

# max 最大值  min 最小值
# get_max
emp = max(list_employees,key = lambda item:item.money)
print(emp.__dict__)

# 升序排列
# sorted(list_employees,key = lambda item:item.money)
# descending_by
# 注意：没有修改原有列表,而是返回新列表
new_list = sorted(list_employees,key = lambda item:item.money,reverse=True)
print(new_list)