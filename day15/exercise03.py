"""
    练习1：创建列表,使用迭代思想,打印每个元素.
	练习2：创建字典,使用迭代思想,打印每个键值对.
"""
list01 = [43, 54, 6, 7, 8]
iterator = list01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

dict01 = {"a": "A", "b": "B", "c": "C"}
iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key, dict01[key])
    except StopIteration:
        break
