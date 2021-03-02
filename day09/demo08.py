"""
    实例(对象)成员
        对象.成员名

        实例变量
            创建
                对象.变量名
            使用
                对象.变量名
            价值
                表达不同对象的不同数据
        实例方法
            创建
                def 方法名(self,参数):
                    ....

            使用
                对象.方法名(参数)

            价值
                操作实例变量
"""
# 写法1:
class Wife:
    def __init__(self, name=""):
        # 创建:对象.变量名 = 数据
        self.name = name

    def play(self):
        print(self.name,"在玩耍")

    def work(self):
        self.play()
        print("在工作")

shuang_er = Wife("双儿")
# 使用:对象.变量名
print(shuang_er.name)
shuang_er.play()# play(shuang_er)
print(shuang_er.__dict__)

jian_ning = Wife("建宁")
# 使用:对象.变量名
print(jian_ning.name)
jian_ning.play()
print(jian_ning.__dict__)

# 写法2:不建议(实例变量应该由类的创造者决定)
# class Wife:
#     pass
#
# shuang_er = Wife()
# # 对象.变量 = 数据
# shuang_er.name = "双儿"
# print(shuang_er.name)

# 写法3:不建议(在__init__中创建实例变量)
# class Wife:
#     def set_name(self,name):
#         self.name = name
#
# shuang_er = Wife()
# shuang_er.set_name("双儿")
# print(shuang_er.name) # ?