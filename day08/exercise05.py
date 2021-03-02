"""
    练习7：创建函数,根据年月计算天数.
            如果2月是闰年,则29天
            　　　 平年    28
    month = int(input("请输入月份:"))
    if 1 <= month <= 12:
        if month == 2:
            print("29天")
        elif month == 4 or month == 6 or month == 9 or month == 11:
            print("30天")
        else:# 1 3 5 7 8 10 12
            print("31天")
    else:
        print("月份有误")

    year = int(input("请输入年份:"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        day = 29
    else:
        day = 28
"""
# def get_day_by_month(month):
#     if 1 <= month <= 12:
#         if month == 2:
#             return 2
#         elif month == 4 or month == 6 or month == 9 or month == 11:
#             return 30
#         else:
#             return 31
#     else:
#         return None

def is_leap_year(year):
    """
        判断是否为闰年
    :param year: 年份
    :return: bool类型,True表达是闰年,False表达不是闰年(是平年)
    """
    # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #     return True
    # return False
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def get_day_by_month(year,month):
    """
        根据月份获取天数
    :param year:年份
    :param month:月份
    :return:天数
    """
    if 1 <= month <= 12:
        if month == 2:
            return 29 if is_leap_year(year) else 28
        if month in (4, 6, 9, 11):
            return 30
        return 31

print(get_day_by_month(2021,2))

