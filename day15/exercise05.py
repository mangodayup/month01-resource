"""
    练习3：创建自定义range类，实现下列效果.
    class MyRange:
        pass

    for number in MyRange(5):
        print(number)# 0 1 2 3 4
"""


# 思考:生成海量数据会不会撑爆内存?
# for number in range(99999999999999999):
#     print(number)  # 0 1 2 3 4

class MyRangeIterator:
    def __init__(self, end):
        self.__number = -1
        self.__end = end

    def __next__(self):
        if self.__number == self.__end - 1:
            raise StopIteration()

        self.__number += 1
        return self.__number


class MyRange:
    def __init__(self, stop):
        self.__stop = stop

    def __iter__(self):
        return MyRangeIterator(self.__stop)

# 循环一次 计算一次  返回一次
for number in MyRange(5):
    print(number)  # 0 1 2 3 4

# mr = MyRange(5)
# iterator = mr.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break
