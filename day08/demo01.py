"""
    多个函数互相调用
"""


def attack():
    print("直拳")
    print("摆拳")
    print("勾拳")
    return 1

def repeat_attack(count):
    result = []
    for __ in range(count):
        res = attack()
        result.append(res)
    return result

res = repeat_attack(2)
print(res)
