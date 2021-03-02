"""
    练习1：创建计算治愈比例的函数
     confirmed = int(input("请输入确诊人数:"))
     cure = int(input("请输入治愈人数:"))
     cure_rate = cure / confirmed * 100
     print("治愈比例为" + str(cure_rate) + "%")
"""


def calculate_cure_rate(confirmed, cure):
    cure_rate = cure / confirmed
    return cure_rate

res = calculate_cure_rate(50, 46)
print(res)

res = calculate_cure_rate(80, 75)
print(res)
