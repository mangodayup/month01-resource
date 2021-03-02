"""
    练习2：定义函数,
         根据生日(年月日),计算活了多天.
    输入：2010   1   1
    输出：从2010年1月1日到现在总共活了3910天
"""
import time


def get_life_days(year, month, day):
    # 思路:
    # 根据生日计算时间戳
    str_time = "%d-%d-%d" % (year, month, day)
    tuple_time = time.strptime(str_time, "%Y-%m-%d")
    # 当前 - 生日
    life_second = time.time() - time.mktime(tuple_time)
    # 秒 -> 天
    return life_second / 60/60 / 24

# 从2010年1月1日到现在总共活了3910天
print(get_life_days(1998, 12, 8))