"""
    练习：创建手机类
          数据：品牌、价格、颜色
          行为：通话
          实例化两个对象并调用其函数
          画出内存图
"""
# 类命名:所有单词首字母大写,不要下划线隔开.
class MobilePhone:
    def __init__(self, brand, price=0, color=""):
        self.brand = brand
        # 生成参数快捷键:alt + 回车
        self.price = price
        self.color = color

    def call(self):
        print(self.brand,"通话")

iphone = MobilePhone("苹果",8000,"白色")
iphone.call()

huawei = MobilePhone("华为",6000,"黑色")
huawei.call()