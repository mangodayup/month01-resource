"""
    迭代 iteration:重复获取下一个元素的过程
    可迭代 iterable:可以被迭代,能够参与for循环
    迭代器 iterator:完成迭代过程的对象
"""
message = "我是齐天大圣"
# for item in message:
#     print(item)

# 迭代(for循环原理)
# 1. 获取迭代器对象
iterator = message.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()
        print(item)
        # 3. 如果停止迭代异常,结束循环
    except StopIteration:
        break

# 面试题:
# 对象能够参与for循环的条件是什么?
# 答1:对象必须具备__iter__函数
# 答2:对象必须是可迭代对象



