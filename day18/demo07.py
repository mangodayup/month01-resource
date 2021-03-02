"""
    装饰器-使用方式
        参数
"""


def new_func(func):
    def wrapper(*args,**kwargs):# 多合一
        print("新功能1")
        result = func(*args,**kwargs)# 一拆多
        # 将旧功能返回值作为内函数的返回值
        return result
    return wrapper

@new_func
def func01(p1):
    print("功能1",p1)
    return 100

@new_func
def func02(p1,p2):
    print("功能2",p1,p2)
    return 200

print(func01(10))# 调用内函数
print(func02(20,30))
print(func02(20,p2 = 30))
