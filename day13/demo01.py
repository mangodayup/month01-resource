"""
    需求:
        一家公司有如下几种岗位:
            程序员:底薪 + 分红
            测试员:底薪 + Bug * 5
            ...
        创建员工管理器,
            -- 存储所有员工
            -- 提供计算总薪资的算法
    封装:创建员工管理器/程序员/测试员
    继承:创建员工类隔离员工管理器与程序员/测试员的变化
    多态:程序员/测试员重写员工类的计算薪资方法实现具体功能

    开闭原则：增加新岗位,员工管理器不变.
    单一职责:
        员工管理器负责统一管理所有员工,获取总薪资.
        程序员类负责程序员的薪资算法
        测试员类负责测试员的薪资算法
    依赖倒置:员工管理器调用员工类,不调用程序员/测试员.
    组合复用:
        员工管理器使用组合关系连接员工薪资算法
        没有通过继承调用员工薪资算法.
    里氏替换:

"""

from typing import List

# ---------架构师----------

class Employee:
    def calculate_salary(self):
        pass

class EmployeeController:
    def __init__(self):
        self.__all_employee = [] # type:List[Employee]

    def add_emp(self, emp:Employee):
        self.__all_employee.append(emp)

    def get_total_salary(self):
        total_salary = 0
        for item in self.__all_employee:
            # 先确定用法
            # 1. 编码时 调用父
            #    运行时 执行子
            total_salary += item.calculate_salary()
        return total_salary




# ---------程序员----------

class Programmer(Employee):
    def __init__(self, base_salay=0, bonus=0):
        self.base_salay = base_salay
        self.bonus = bonus

    # 后确定做法(符合/遵守 用法)
    # 2. 子重写
    def calculate_salary(self):
        return self.base_salay + self.bonus


class Tester(Employee):
    def __init__(self, base_salary=0, bug_count=0):
        self.base_salary = base_salary
        self.bug_count = bug_count

    def calculate_salary(self):
        return self.base_salary + self.bug_count * 5


# 入口
controller = EmployeeController()
# 3. 创建子
controller.add_emp(Programmer(10000, 1000000))
controller.add_emp(Tester(8000, 2000))
print(controller.get_total_salary())
