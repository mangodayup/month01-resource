"""
练习1：定义函数,根据年月日,计算星期。
输入：2020   9   15
输出：星期二
"""
import time


def get_week_name(year,month,day):
    """

    :param year:
    :param month:
    :param day:
    :return:
    """
    # 根据三个变量年月日计算时间元组
    str_time = "%d-%d-%d"%(year,month,day)
    tuple_time = time.strptime(str_time, "%Y-%m-%d")
    # 从时间元组中获取星期索引
    index = tuple_time[-3]
    # 将星期索引转换为文字
    tuple_week = ("星期一","星期二","星期三","星期四","星期五","星期六","星期日")
    return tuple_week[index]


print(get_week_name(2021, 1, 19))