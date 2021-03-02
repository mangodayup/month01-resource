"""
    生成器练习
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
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]


# 练习1：定义函数,在员工列表中查找姓名是
#       三个字的所有员工
def find_employees_by_name():
    for item in list_employees:
        if len(item.name) == 3:
            yield item

# 练习2：定义函数,在员工列表中查找员工编号
#       是1003的员工
def find_employees_by_eid():
    for item in list_employees:
        if item.eid == 1003:
            return item

# 练习3：定义函数,在员工列表中查找部门是
#       9002的所有员工
def find_employees_by_did():
    for item in list_employees:
        if item.did == 9002:
            yield item
# 练习4：定义函数,在员工列表中查找所有员工
#       的姓名
def find_employees_name():
    for item in list_employees:
        yield item.name



# 测试
result = find_employees_by_name()
for emp in result:
    print(emp.__dict__)


# 生成器不支持索引切片
# print(result[-1])

# 解决方案：将生成器转换为容器
result = tuple(find_employees_by_name())
print(result[-1].__dict__)

emp = find_employees_by_eid()
print(emp.__dict__)

for item in find_employees_by_did():
    print(item.__dict__)

result = list(find_employees_name())
print(result[:3])

# 练习5：使用生成器表达式完成上述功能
result = (item for item in list_employees if len(item.name) == 3)
for emp in result:
    print(emp.__dict__)

result = (item for item in list_employees if item.did == 9002)
for emp in result:
    print(emp.__dict__)

result = (item.name for item in list_employees)
for emp in result:
    print(emp)

