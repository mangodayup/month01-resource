"""
    累加1--100之间所有整数
    条件:能被3整除
"""
# 思想: 满足条件累加.
sum_value = 0
for item in range(1, 101):
    if item % 3 == 0:
        sum_value += item
print(sum_value)

# 思想: 不满足条件跳过,否则累加.
sum_value = 0  # 1 2 3 ...
for item in range(1, 101):
    if item % 3 != 0:
        continue  # 跳过:继续下次循环
        # break  # 跳出:结束循环
    sum_value += item
print(sum_value)
