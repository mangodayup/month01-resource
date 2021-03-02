"""
    练习1：定义函数,在列表中找出所有偶数
    [43,43,54,56,76,87,98]
    练习2. 定义函数,在列表中找出所有数字
     [43,"悟空",True,56,"八戒",87.5,98]
"""
def get_evens(target):
    for number in target:
        if number % 2 ==0:
            yield number


list01 = [3, 34, 45, 56, 67, 7, 89, 8]
re01 = get_evens(list01)
for item in re01:
    print(item)


def get_numbers(target):
    for number in target:
        if type(number) in (int,float):
            yield number


list01 = [3, 34, 45, 56, 67, 7, 89, 8]
re01 = get_evens(list01)
for item in re01:
    print(item)