"""
    练习1：以面向对象思想,描述下列情景.
    小明请保洁打扫卫生
    要求:使用三种方法实现跨类调用
"""

"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def notify(self):
        print("发出通知")
        cleaner = Cleaner()
        cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")


xm = Person("小明")
xm.notify()
"""

"""
class Person:
    def __init__(self, name=""):
        self.name = name
        self.cleaner = Cleaner()

    def notify(self):
        print("发出通知")
        self.cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")

xm = Person("小明")
xm.notify()
"""

class Person:
    def __init__(self, name=""):
        self.name = name

    def notify(self,service):
        print("发出通知")
        service.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")

xm = Person("小明")
cleaner = Cleaner()
xm.notify(cleaner)