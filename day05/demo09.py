"""
    1.	列表转换为字符串：
	result = "连接符".join(列表)
"""
list01 = ["a", "b", "c"]
result = "-".join(list01)
print(result)

# 根据需求拼接字符串
# 缺点:每次拼接都会产生新字符串,使旧字符串成为垃圾.
result = ""
for number in range(10):  # 0 1 2
    # 0
    # 01
    # 012
    result += str(number)
print(result)
# 解决:将字符串拼接改为列表追加
# 思想:将对不可变数据的频繁修改,
#      改为对可变数据的修改
result = []
for number in range(10):
    result.append(str(number))
result = "".join(result)
print(result)
# 练习：
#     在终端中,循环录入字符串,如果录入空则停止.
#     停止录入后打印所有内容(一个字符串)
# 效果：
# 	请输入内容：香港
#   请输入内容：上海
#   请输入内容：新疆
#   请输入内容：
#   香港_上海_新疆
