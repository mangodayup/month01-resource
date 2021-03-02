"""
    练习5：创建函数,计算IQ等级
    ma = int(input("请输入你的心里年龄："))
    ca = int(input("请输入你的实际年龄："))
    iq = ma / ca * 100
    if 140 <= iq:
        print("天才")
    elif 120 <= iq:
        print("超常")
    elif 110 <= iq:
        print("聪慧")
    elif 90 <= iq:
        print("正常")
    elif 80 <= iq:
        print("迟钝")
    else:
        print("低能")
"""


def get_iq_level(ma, ca):
    """
        获取智商等级
    :param ma:心理年龄,int类型
    :param ca:实际年龄,int类型
    :return:智商等级,str类型
    """
    iq = ma / ca * 100
    if 140 <= iq:
        return "天才"
    if 120 <= iq:
        return "超常"
    if 110 <= iq:
        return "聪慧"
    if 90 <= iq:
        return "正常"
    if 80 <= iq:
        return "迟钝"
    return "低能"

# def get_iq_level(ma, ca):
#     iq = ma / ca * 100
#     if 140 <= iq:
#         return "天才"
#     el表达满足上面条件,不执行本行
#     但是上面的return执行后函数退出
#     所以el多余
#     elif 120 <= iq:
#         return "超常"
#     elif 110 <= iq:
#         return "聪慧"
#     elif 90 <= iq:
#         return "正常"
#     elif 80 <= iq:
#         return "迟钝"
#     else:
#         return "低能"

print(get_iq_level(23,20))
