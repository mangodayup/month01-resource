"""
    lambda 表达式
        匿名函数
        匿名函数支持的功能,有名函数都支持.
        但是匿名函数只能有一句话，且不能是赋值语句。
"""
# 写法1：有参数有返回值
# def func01(p1,p2):
#     return p1 > p2

func01 = lambda p1, p2: p1 > p2

print(func01(10, 20))

# 写法2：无参数有返回值
# def func02():
#     return 100

func02 = lambda: 100

print(func02())

# 写法3：有参数无返回值
# def func03(p1):
#     print("参数是：",p1)

func03 = lambda p1: print("参数是：", p1)

func03(10)

# 写法4：无参数无返回值
# def func04():
#     print("func04")

func04 = lambda: print("func04")

func04()


# 注意1：lambda 不支持赋值语句
def func05(p1):
    p1[0] = 2

# func05 = lambda p1:p1[0] = 2

list01 = [1]
func05(list01)
print(list01)  # [2]

# 注意2:lambad 函数体只能有一句话
def func06():
    for item in range(3):
        print(item)


# func06 = lambda :for item in range(3):print(item)
func06()