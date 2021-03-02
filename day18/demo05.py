"""
    装饰器-使用方式
        @new_func
"""


def new_func(func):
    def wrapper():
        print("新功能1")  # 执行新功能
        func()  # 执行旧功能

    return wrapper

@new_func
# func01 = new_func(func01)
def func01():
    print("功能1")

func01()
