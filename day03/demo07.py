"""
    bool 转换
        结果为False:int  float  str
                    0    0.0    ""
        核心:有值则为True

    if真值表达式
        if 值:
            有值满足条件
"""
print(bool(""))
if -5:  # bool(-5)
    print("ok")

# 判断在终端中输入的内容是否有值
content = "xxx"
# if content != "":
# if content != 0:
# if content != 0.0:
if content:  # 有值
    print("输入的是:" + content)
