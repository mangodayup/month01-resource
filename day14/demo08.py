"""
    标准库模块
        时间
"""
import time

# 人类时间:公元元年~2021年1月19日 16:34:05
# -221
# 机器时间:1970年元旦~1611045288.4559357

# 1.获取当前机器时间 - 时间戳(单位是秒)
print(time.time())  # 1611045288.4559357
# 2.获取当前人类时间 - 时间元组(年/月/日/时/分/秒/星期/一年第一几天/是否夏令时)
time_tuple = time.localtime()
print(time_tuple)
# 3. 时间戳 -> 时间元组
# 时间元组 = time.localtime(时间戳)
print(time.localtime(1611045288.4559357))
# 4. 时间元组 -> 时间戳
print(time.mktime(time_tuple))
# 5. 时间元组 -> 字符串
print(time.strftime("%y-%m-%d %H:%M:%S",time_tuple))
# 2021-01-19 16:56:08
print(time.strftime("%Y-%m-%d %H:%M:%S",time_tuple))
# 6. 字符串 -> 时间元组
print(time.strptime("2021-01-19 16:56:08", "%Y-%m-%d %H:%M:%S"))