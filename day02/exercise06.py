"""
    练习：在终端中输入商品单价、购买的数量和支付金额。计算应该找回多少钱。
    效果：
        请输入商品单价：5
        请输入购买数量：3
        请输入支付金额：20
        应找回：5.0
"""
price = int(input("请输入商品单价："))
count = int(input("请输入购买数量："))
money = float(input("请输入支付金额："))
result = money - price * count
print("应找回：" + str(result))
