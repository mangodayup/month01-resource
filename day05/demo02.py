"""
    切片
        作用:
            定位多个元素
        语法1:
            容器名[开始:结束:间隔]
            注意不包含结束值
        语法2:
            容器名[开始:结束]
            注意间隔默认为1
        语法3:
            容器名[:结束]
            开始默认0
        语法4:
            容器名[:]
            结束默认包含末尾值
"""
# range(开始,结束,间隔)
message = "我是花果山齐天大圣"
print(message[2:5:1])  # 花果山
print(message[2:-4:1])  # 花果山
print(message[2:-4])  # 花果山
print(message[:-4])  # 我是花果山
print(message[:])  # 我是花果山齐天大圣
print(message[-3:])  # 天大圣

message = "我是花果山齐天大圣"
print(message[:2])
print(message[-2:])
print(message[1: 5])
print(message[-2: 3:-1])  # 大天齐山
print(message[1: 1])  # 空
print(message[2: 5:-1])  # 空
# 特殊:翻转
print(message[::-1])  # 圣大天齐山果花是我
