"""
    练习3：创建函数,根据课程阶段计算课程名称.
    number = input("请输入课程阶段数：")
    if number == "1":
        print("Python语言核心编程")
    elif number == "2":
        print("Python高级软件技术")
    elif number == "3":
        print("Web全栈")
    elif number == "4":
        print("网络爬虫")
    elif number == "5":
        print("数据分析、人工智能")
"""


def get_course_name(number):
    """
        获取课程名称
    :param number:int类型,课程阶段编号
    :return:课程名称
    """
    tuple_coures = (
        "Python语言核心编程",
        "Python高级软件技术",
        "Web全栈",
        "网络爬虫",
        "数据分析、人工智能"
    )
    if 1 <= number <= len(tuple_coures):
        return tuple_coures[number - 1]


print(get_course_name(10))
