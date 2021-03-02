"""
    元组应用
"""

month = int(input("请输入月份:"))
if 1 <= month <= 12:
    if month == 2:
        print("29天")
    # elif month == 4 or month == 6 or month == 9 or month == 11:
    elif month in (4, 6, 9, 11):
        print("30天")
    else:
        print("31天")
else:
    print("月份有误")

# 将每月的天数存入元组
day_of_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
print(day_of_month[0])
print(day_of_month[2])
