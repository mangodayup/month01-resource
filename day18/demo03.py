"""
    闭包应用
        逻辑连续
            从获得压岁钱,
            到不断购买的过程不中断可持续
"""

def give_gife_money(money):
    print(f"获得了{money}元压岁钱")

    def child_buy(commodity, price):
        nonlocal money
        money -= price
        print(f"购买{commodity}花了{price},还剩下{money}")

    return child_buy


action = give_gife_money(1000)
action("遥控汽车", 300)
action("遥控飞机", 500)
action("变形金刚", 200)
