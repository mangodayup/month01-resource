"""
    while 条件1:
        循环体
        if 条件2:
            break
    else:
        不满足条件1执行的逻辑
        从条件2退出,不执行当前逻辑

    猜数字2.0
        最多猜3次,如果超过次数,提示"游戏失败"
"""
import random

random_number = random.randint(1,100)
count =0
while count < 3:
    count += 1
    input_number = int(input("请输入数字:"))
    if input_number > random_number:
        print("大了")
    elif input_number<random_number:
        print("小了")
    else:
        print("恭喜猜对啦,总共猜了"+str(count)+"次")
        break
else:
    print("游戏失败")

