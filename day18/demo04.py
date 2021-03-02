"""
    闭包最佳实践 - 装饰器
        1. 有外有内：外函数负责存储旧功能
        2. 内使用外：内函数负责执行新旧功能
        3. 外返回内：不断执行新与旧
        价值：
            可装可卸
"""


# 为旧功能(func01/func02)
# 增加新功能(new_func)
def func01():
    print("功能1")


def func02():
    print("功能2")


# 装饰器：
def new_func1(func):
    def wrapper():
        print("新功能1")  # 执行新功能
        func()  # 执行旧功能

    return wrapper


def new_func2(func):
    def wrapper():
        print("新功能2")  # 执行新功能
        func()  # 执行旧功能

    return wrapper


# 旧功能 = 新功能
# func01 = new_func # 覆盖了旧功能
# new_func(func01) # 此时执行了新旧功能

# 调用外函数包装新与旧
func01 = new_func1(func01)

# func02包装两种功能
func02 = new_func1(func02)
func02 = new_func2(func02)

# 调用内函数执行新与旧
func01()
func01()
func02()
func02()
