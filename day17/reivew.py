"""
    函数式编程
        应用1：将函数作为参数
        特征：
            1. 分
        思想：
            def 功能1():
                通用代码
                变化点1

            def 功能2():
                通用代码
                变化点2

            1. 分：单独定义函数
            def 变化点1():
                ...

            def 变化点2():
                ...

            2. 隔：用参数抽象、统一
            def 通用功能(参数):
                通用代码
                参数()

            3. 做：将新功能的变化点定义到函数中
            def 变化点3():
                ...

            通用功能(变化点3)
"""
from common.iterable_tools import IterableHelper


# 参数是：列表的每个元素
# 返回值：通用函数的判断条件
def condition01(number):
    return number % 2


list01 = [43, 45, 56, 6, 7]
for item in IterableHelper.find_all(list01, condition01):
    print(item)
