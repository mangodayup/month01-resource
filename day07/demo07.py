"""
    返回值语法
"""
def func01():
    print("func01执行了")
    return 100

# 1. 调用者,可以接收也可以不接收返回值
func01()
res = func01()
print(res)

# 2.在Python语言中,
# 函数没有return或return后面没有数据,
# 都相当于return None
def func02():
    print("func02执行了")
    return

res = func02()
print(res) # None

# 3.return可以退出函数
def func03():
    print("func03执行了")
    return
    print("func03又执行了")

func03()

# 4. return 可以退出多层循环嵌套
def func04():
    while True:
        while True:
            while True:
                # break 只能退出一层循环
                print("循环体")
                return

func04()
