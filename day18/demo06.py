"""
    装饰器-使用方式
        返回值
            将旧功能返回值作为内函数的返回值
"""


def new_func(func):
    def wrapper():
        print("新功能1")
        result = func()
        # 将旧功能返回值作为内函数的返回值
        return result

    return wrapper

@new_func
def func01():
    print("功能1")
    return 100

@new_func
def func02():
    print("功能2")
    return 200

print(func01())# 调用的是内函数
print(func02())
