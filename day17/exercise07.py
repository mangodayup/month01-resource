"""
    练习8：
        需求：
            定义函数,根据薪资对员工列表进行降序排列
            定义函数,根据编号对员工列表进行降序排列
        步骤：
            1.在IterableHelper中创建
               通用函数 is_repeat
            2. 使用lambda在当前模块中调用
"""
from common.iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money


# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

IterableHelper.descending_by(list_employees,lambda item:item.money)

print(list_employees)

