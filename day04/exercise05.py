"""
    练习:
    在终端中输入任意整数，计算累加和.
    "1234" -> "1" -> 累加 1
    效果：
    	请输入一个整数:12345
      累加和是 15
"""
str_number = input("请输入整数:")
sum_value = 0
for item in str_number:
    sum_value += int(item)
print(sum_value)
