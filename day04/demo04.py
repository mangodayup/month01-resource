"""
   for - 循环计数
        range 函数:整数生成器
"""
# 写法1:range(开始,结束,间隔)
# 注意:不包含结束值
for item in range(1, 3, 1):
    print(item)
# 写法2:range(开始,结束)
# 注意:间隔默认为1
for item in range(1, 3):
    print(item)
# 写法3:range(结束)
# 注意:开始默认为0
for item in range(3):
    print(item)
