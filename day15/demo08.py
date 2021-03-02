"""
    生成器应用
"""


# 需求:定义函数,在列表中查找大于10的数字
# 传统思想:创建容器存储所有结果
def get_number_gt_10(target):
    result = []
    for number in target:
        if number > 10:
            result.append(number)
    return result


list01 = [3, 34, 45, 56, 67, 7, 89, 8]
re01 = get_number_gt_10(list01)
for item in re01:
    print(item)


# 生成器思想:通过yield返回结果
def get_number_gt_10(target):
    for number in target:
        if number > 10:
            yield number


list01 = [3, 34, 45, 56, 67, 7, 89, 8]
re01 = get_number_gt_10(list01)
for item in re01:
    print(item)
