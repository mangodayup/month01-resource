"""
    练习3：
    在终端中输入课程阶段数,显示课程名称
    1 显示 Python语言核心编程
    2 显示 Python高级软件技术
    3 显示 Web 全栈
    4 显示 网络爬虫
    5 显示 数据分析、人工智能
"""
number = int(input("请输入课程阶段数："))
if number == 1:
    print("Python语言核心编程")
elif number == 2:
    print("Python高级软件技术")
elif number == 3:
    print("Web 全栈")
elif number == 4:
    print("网络爬虫")
elif number == 5:
    print("数据分析、人工智能")

# 没有互斥,如果前面条件满足,后面条件依然需要判断
# if number == 1:
#     print("Python语言核心编程")
# if number == 2:
#     print("Python高级软件技术")
# if number == 3:
#     print("Web 全栈")
# if number == 4:
#     print("网络爬虫")
# if number == 5:
#     print("数据分析、人工智能")
