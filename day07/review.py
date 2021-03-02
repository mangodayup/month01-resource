"""
    小结 - 容器
        一.种类与特点
            字符串：存储字符的编码,不可变,序列
            列表：存储变量,可变,序列
            元组：存储变量,不可变,序列
            字典：存储键值对,可变,散列
                 键的限制：唯一且不变(字符串、元组、数值)
            集合：存储键,可变,散列

        二.可变与不可变
            面试题1：Python有多少种数据类型
            答：只有2种,根据内存存储机制可与分为可变不可变.
                可变：预留空间 + 自动扩容
                    例如：list  dict  set...
                不可变：按需分配
                    例如：str 数值 bool tuple ...
            面试题2：既然有可变数据为什么还存在不可变数据?
                不可变数据性能更高,应该优先选择.
                (存储相同数据内存更少,创建速度更快)

        三.序列与散列
            序列:有顺序,空间连续(省地),定位灵活(索引切片),定位单个元素较慢
            散列:无顺序,数据分布松散(费地),定位单个元素最快

        四.基础操作

"""
# 1. 创建
list01 = [10, 20, 30]
dict01 = {"a": "A", "b": "B"}

# 2. 添加
list01.append(40)
list01.insert(0, 50)
dict01["c"] = "C"

# 3. 定位
print(list01[0])
print(list01[-2:])
print(dict01["a"])

# 4. 遍历
for item in list01:
    print(item)

for i in range(len(list01) - 1, -1, -1):
    print(list01[i])

for key in dict01:
    print(key)

for value in dict01.values():
    print(value)

for k, v in dict01.items():
    print(k)
    print(v)

# 5. 删除
list01.remove(10)
del list01[-1]

del dict01["a"]

# 6. 相互转换
# list --> dict
# 要求：列表中的元素必须能一分二
print(dict([(1,2), (3,4)]))

# dict-->list
print(list(dict01))
print(list(dict01.values()))
print(list(dict01.items()))
