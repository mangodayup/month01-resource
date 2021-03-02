"""
    可迭代对象工具集
       从学习角度将：理解函数式编程思想(分、隔、做)
       从功能角度将：功能无限强大
       从面试角度将：在简历中写明：“精通函数式编程”
                  来源于微软的Linq框架
        步骤：
            1. 根据需求，写出函数。
            2. 因为主体逻辑相同,核心算法不同.
               所以使用函数式编程思想(分、隔、做)
               创建通用函数select
               定义在IterableHelper中
            3. 使用lambda在当前模块中调用
"""


class IterableHelper:
    """
        集成操作框架
        可迭代对象助手
    """
    @staticmethod
    def find_all(iterable, condition):
        """
            根据条件在可迭代对象找查找所有元素
        :param iterable:可迭代对象
        :param condition:函数类型的条件
        :return:生成器,推算满足条件的元素
        """
        for item in iterable:
            if condition(item):
                yield item

    @staticmethod
    def find_single(iterable, condition):
        """
            根据条件在可迭代对象找查找单个元素
        :param iterable:可迭代对象
        :param condition:函数类型的条件
        :return:满足条件的单个元素
        """
        for item in iterable:
            if condition(item):
                return item

    @staticmethod
    def select(iterable, handle):
        """
            对可迭代对象中每个元素进行处理,返回处理结果
        :param iterable:可迭代对象
        :param handle:函数类型的处理逻辑
        :return:生成器,推算所有元素的处理结果
        """
        for item in iterable:
            yield handle(item)

    @staticmethod
    def get_count(iterable, condition):
        """
            获取可迭代对象中满足条件的元素数量
        :param iterable:可迭代对象
        :param condition:函数类型的条件
        :return:数量
        """
        count = 0
        for item in iterable:
            if condition(item):
                count += 1
        return count

    @staticmethod
    def sum(iterable, handle):
        """
            根据指定逻辑累加可迭代对象元素
        :param iterable:可迭代对象
        :param handle:函数类型的处理逻辑
        :return:累加结果
        """
        sum_value = 0
        for item in iterable:
            # sum_value += item.eid
            sum_value += handle(item)
        return sum_value

    @staticmethod
    def delete_all(iterable, condition):
        """
            在可迭代对象中删除满足条件的元素
        :param iterable: 可迭代对象
        :param condition: 函数类型的条件
        :return:删除数量
        """
        count = 0
        for i in range(len(iterable) - 1, -1, -1):
            if condition(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def get_max(iterable, condition):
        """
            根据条件在可迭代对象中获取最大元素
        :param iterable:可迭代对象
        :param condition:函数类型的条件
        :return:最大元素
        """
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if condition(max_value) < condition(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def descending_by(iterable, condition):
        """
            根据条件对象可迭代对象进行降序排列
        :param iterable: 可迭代对象
        :param condition: 函数类型的条件
        """
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if condition(iterable[r]) < condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]

    @staticmethod
    def is_repeat(iterable,condition):
        """
            根据条件判断可迭代对象中是否有重复
        :param iterable:可迭代对象
        :param condition: 函数类型的条件
        :return: bool类型,True有重复,False没重复
        """
        for r in range(len(iterable)-1):
            for c in range(r+1,len(iterable)):
                if condition(iterable[r]) == condition(iterable[c]):
                    return True # 有重复
        return False # 没重复