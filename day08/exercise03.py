"""
    练习4：创建函数,计算梯形面积.
        top_base = float(input("请输入上底："))
        bottom_base = float(input("请输入下底："))
        height = float(input("请输入高："))
        result = (top_base + bottom_base) * height / 2
        print("梯形面积是：" + str(result))
"""
def calculate_trapezoid_area(top_base, bottom_base, height):
    """
        计算梯形面积
    :param top_base:上底
    :param bottom_base:下底
    :param height:高
    :return:面积
    """
    return (top_base + bottom_base) * height / 2

# 调用函数：
#   函数名称(具体数据)
print(calculate_trapezoid_area(2, 3, 4))
