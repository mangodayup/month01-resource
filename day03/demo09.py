"""
    while 循环
        写法1:
            while True:
                循环体
                if 条件:
                    break

"""
# 死循环
while True:
    if input("请输入您的职业") == "老师":
        print("教师节快乐")
    else:  # 否则(互斥)
        print("与你无关")

    if input("请输入q键退出:") == "q":
        break  # 跳出循环
