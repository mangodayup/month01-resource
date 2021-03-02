"""
    函数参数
        形式参数
            星号元组形参
"""


# 位置实参数量可以无限
def func01(*args):
    print(args)


func01()  # 空元组
func01(1, 2, 34)  # (1, 2, 34)
# 不支持关键字实参
# func01(args = 1,a=1)
