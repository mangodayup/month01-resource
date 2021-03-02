"""
    可迭代对象工具集
"""


class IterableHelper:
    @staticmethod
    def find_all(iterable, condition):
        """
            根据条件在可迭代对象找查找元素
        :param iterable:可迭代对象
        :param condition:函数类型的条件
        :return:生成器,推算满足条件的元素
        """
        for item in iterable:
            if condition(item):
                yield item
