"""
    练习2：定义函数,根据总两数,计算几斤零几两.:
          提示：使用容器包装需要返回的多个数据
    total_liang = int(input("请输入两:"))
    jin = total_liang // 16
    liang = total_liang % 16
    print(str(jin) + "斤零" + str(liang) + "两")
"""


def get_weight(total_liang):
    """
        获取重量
    :param total_liang:总量数
    :return:元组(斤,两)
    """
    jin = total_liang // 16
    liang = total_liang % 16
    return jin, liang

jin, liang = get_weight(100)
print(str(jin) + "斤零" + str(liang) + "两")

