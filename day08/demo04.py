"""
    函数参数
        实际参数
        形式参数
"""


def fun01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)

# 位置形参:实参必填
# 默认形参:实参可选
# 注意2:默认形参必须从右向左依次存在
def func02(p1 =0, p2="", p3=100):
    print(p1)
    print(p2)
    print(p3)

# 1. 位置实参:根据顺序与形参进行对应
fun01(1, 2, 3)

# 2. 关键字实参:根据名字与形参进行对应
fun01(p1=1, p2=2, p3=3)
fun01(p2=2, p1=1, p3=3)

# fun01(p2=2, p1=1)
# TypeError: fun01() missing 1 required positional argument: 'p3'

# fun01(1, 2) # 缺少参数
# TypeError: fun01() takes 3 positional arguments but 4 were given
# fun01(1, 2, 3, 4) # 参数过多

func02(p2=2)
func02(p2=2,p3=3)
# 支持同时使用位置实参与关键字实参
func02(1,p3=3)
# 注意1:先位置实参,后关键字实参
# func02(p1 =1,2,3)



