"""
    练习4：定义函数，将列表中大于某个值的元素设置为None
             参数                           结果
   [34, 545, 56, 7, 78, 8]  -10->  [None,None,None,7,None,8]
   [34, 545, 56, 7, 78, 8]  -100->  [34, None, 56, 7, 78, 8]
"""


def update_data(list_target, value):
    """

    :param list_target:
    :param value:
    :return:
    """
    for i in range(len(list_target)):
        if list_target[i] > value:
            list_target[i] = None

list01 = [34, 545, 56, 7, 78, 8]
update_data(list01,10)
print(list01)


