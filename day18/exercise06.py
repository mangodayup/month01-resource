"""
    练习2：
        为sum_data,增加打印函数执行时间的功能.
        函数执行时间公式：
            执行后时间 - 执行前时间
"""
import time


def print_execute_time(func):
    print("外函数内")

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print("执行时间：", stop - start)
        return result

    return wrapper


@print_execute_time
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value


print(sum_data(10))
print(sum_data(1000000))
