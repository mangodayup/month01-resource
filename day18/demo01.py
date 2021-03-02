"""
    Enclosing外部嵌套作用域 ：函数嵌套。
"""
def func01():
    # 局部作用域：相对函数外
    # 外部嵌套作用域：相对内部函数
    print("func01")
    a = 10
    def func02():
        print("func02")
        # 内部函数,可以读取外函数变量
        print(a)

    func02()

# 不能在外函数外部，访问内部函数
# 只能在外函数内部
func01()


def func03():
    a = 10

    def func04():
        # 内函数不能修改外函数变量
        # a = 20
        # 必须通过nonlocal声明
        nonlocal a
        a = 20

    func04()
    print(a)

func03()