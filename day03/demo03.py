"""
    逻辑运算符
        与或非:判断两个命题关系
"""
# 与and 一假俱假 并且关系(都满足结论才满足)
print(True and True)  # True
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False

# 案例:
# 有钱吗? 并且 有房吗?
# print(int(input("请输入现金:")) > 100000 and input("请输入房产:") == "有")

# 与or 一真俱真 或者关系(满足一个就行)
print(True or True)  # True
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False
# 案例:
# 有钱吗? 或者 有房吗?
print(int(input("请输入现金:"))
      > 100000 or
      input("请输入房产:") == "有")

# 非:取反
print(not True)  # False
