"""
    算法：
        1. 变量交换
            a,b = b,a
        2. 取最值
            list01 = [.....]
            max_value = list01[0]
            for i in range(1,len(list01)):
                if max_value < list01[i]:
                    max_value = list01[i]
        3. 累计运算
            初始值 = ?
            循环 ....
                初始值 += ?
            结果
        4. 自定义排序算法
"""
list01 = [54, 545, 6, 76, 8, 2, 9]
# 升序：小 --> 大
# 降序：大 --> 小
# 思想：
#   容器中所有元素两两比较
# 步骤：
#   在整个范围内,让第一个元素为最小值
# min_value = list01[0]
# for i in range(1, len(list01)):
#     if min_value > list01[i]:
#         min_value = list01[i]
# print(min_value)

# for i in range(1, len(list01)):
#     if list01[0] > list01[i]:
#         list01[0], list01[i] = list01[i], list01[0]
#
# for i in range(2, len(list01)):
#     if list01[1] > list01[i]:
#         list01[1], list01[i] = list01[i], list01[1]

# [取]出数据
for r in range(len(list01) - 1):
    # [比]较最小值
    for c in range(r + 1, len(list01)):
        # 如果发现更小
        if list01[r] > list01[c]:
            # 交换
            list01[r], list01[c] = list01[c], list01[r]
print(list01)


