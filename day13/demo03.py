"""
       A
      / \
     /   \
    B     C
     \   /
      \ /
       D
"""


class A:
    def func01(self):
        print("A")


class B(A):
    def func01(self):
        print("B")
        super().func01()


class C(A):
    def func01(self):
        print("C")
        super().func01()


class D(B, C):
    def func01(self):
        print("D")
        super().func01()

d = D()
# D -> B -> C -> A
d.func01()
# 
print(D.mro())
