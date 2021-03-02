"""
    函数参数
        实际参数
"""


def func01(p1, p2, p3):
    print(p1, p2, p3)

# 序列实参:拆,按照顺序与形参对应
list01 = [1, 2, 3]
name = "孙悟空"
tuple01 = (4, 5, 6)
# func01(list01)
func01(*list01)  # 拆  1, 2, 3
func01(*name)  # 拆  孙 悟 空
func01(*tuple01)  # 拆  4, 5, 6

# 字典实参:拆,按照名称与形参对应
dict01 = {"p2":"B","p1":"A","p3":"C"}
func01(**dict01)