"""
    函数式编程
        理论支柱：函数可以直接赋值给变量
        应用：
            将函数作为参数
"""


def func01():
    print("func01")


# 直接调用函数
func01()
# 将返回值赋值给变量
# a = func01()

# 将函数赋值给变量
a = func01
# 间接调用函数
a()


def func02():
    print("func02")


def func03(func):
    print("func03")
    # func02() # 直接调用 - 固定(创建时)
    func()  # 间接调用 - 灵活(使用时)


def func04(p1):
    print("func04参数是:", p1)


func03(func02)
func03(func01)
# 因为func04具有参数所以不能传递给func03
# func03(func04)
