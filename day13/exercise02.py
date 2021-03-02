class A:
    def func01(self):
        print("A")
        super().func01()


class B:
    def func01(self):
        print("B")


class C(A, B):
    def func01(self):
        print("C")
        super().func01()


class D(A, B):
    def func01(self):
        print("D")
        super().func01()


class E(C, D):
    def func01(self):
        print("E")
        # super().func01()
        # 如果指定某个父类的同名方法
        # 需要使用类名.实例方法名(self)
        D.func01(self)


e = E()
e.func01()  # E -> C -> D -> A -> B
