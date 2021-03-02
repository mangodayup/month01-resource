"""
    函数参数
        形式参数
            命名关键字形参
"""

# 命名关键字形参:
#   星号元组形参后面的位置形参
#   限制实参必须是关键字实参
def func01(*args, p1, p2):
    print(args)
    print(p1)
    print(p2)


func01(p1=1, p2=2)
func01(1, 2, 3, p1=1, p2=2)


def func02(p1, *, p2=0):
    print(p1)
    print(p2)


# 通常星号后面的命名关键字形参属于辅助参数,可选.
func02(1)
func02(1, p2=2)

# 应用
# print(10)
# print("a")
# print(True)
print(10, "a", True)
# def print(*value, sep=' ', end='\n'):
print(100, "量是", 6, "斤", 4, "两")
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
print(100, "量是", 6, "斤", 4, "两", sep="")
print(100, "量是", sep="", end=" ")
# print(100,"量是",""," ")
