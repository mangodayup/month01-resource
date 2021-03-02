# 练习：说出程序执行结果.
def func01(list_target):
    print(list_target)  # [1, 2, 3]


def func02(*args):  # 三合一  接受到的是一个元组
    print(args)  # (1,2,3)


def func03(*args, **kwargs):  # 实参数量无限
    print(args)  # (1,2,3)
    print(kwargs)  # {"a":4,"b":5,"c":6}


def func04(p1, p2, *, p4, **kwargs):
    print(p1)  # 10
    print(p2)  # 20
    print(p4)  # 30
    print(kwargs)  # {"p5" : 40}


func01([1, 2, 3])
func02(*[1, 2, 3])  # 一拆三 实际传递的是3个整数
func03(1, 2, 3, a=4, b=5, c=6)  # 先位置实参后关键字实参
func04(10, 20, p4=30, p5=40)
