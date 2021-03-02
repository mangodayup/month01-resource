"""
    异常处理
        适用性:不解决语法错误,
              而是解决逻辑错误.
        现象：当异常发生时，
             程序不会再向下执行，
             而转到函数的调用语句。
"""
# 语法错误(异常):程序员写错了代码
# NameError
# print(qtx)

# TypeError
# print("1" + 1)

class Wife:
    pass

w01 = Wife()
# AttributeError
# print(w01.name)

# 逻辑错误:运行时因为数据超过意料之外而引发的错误
def div_apple(apple_count):
    # ValueError
    person_count = int(input("请输入人数:"))
    # ZeroDivisionError
    result = apple_count / person_count
    print(f"每人{result}个苹果")

def main():
    div_apple(10)

main()

print("后续逻辑")
