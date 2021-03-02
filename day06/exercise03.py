# 3月10日
# 31 + 29 + 10
# 练习2：
#     根据月日,计算是这一年的第几天.
#     公式：前几个月总天数 + 当月天数
# 例如：5月10日
#     计算：31  29  31  30 + 10
month = int(input("请输入月份:"))  # 5
day = int(input("请输入天:"))
day_of_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# total_days = 0
# for i in range(4):# 0 1 2 3
#     total_days += day_of_month[i]
# total_days = sum(day_of_month[:4])
total_days = sum(day_of_month[:month - 1])
total_days += day
print(total_days)
