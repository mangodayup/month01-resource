"""
    异常处理
        处理目的:将向上翻的状态改为向下执行
        核心意义:
            保障程序按照既定流程执行
        本质:快速传递错误消息
            抛出  -->  接受
"""


# 写法1:包治百病
def div_apple(apple_count):
    try:
        # ValueError
        person_count = int(input("请输入人数:"))
        # ZeroDivisionError
        result = apple_count / person_count
        print(f"每人{result}个苹果")
    except Exception:
        print("程序出错了")

# 2. 对症下药
# def div_apple(apple_count):
#     try:
#         # ValueError
#         person_count = int(input("请输入人数:"))
#         # ZeroDivisionError
#         result = apple_count / person_count
#         print(f"每人{result}个苹果")
#     except ValueError:
#         print("输入的不是整数")
#     except ZeroDivisionError:
#         print("输入的是零")

# 3. 无论是否异常,一定执行的逻辑
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数:"))
#         result = apple_count / person_count
#         print(f"每人{result}个苹果")
#         # 打开文件-开门
#         # 处理文件
#     finally:
#         # 关闭文件-关门
#         print("分苹果结束")

# 4. 没有异常时执行
# def div_apple(apple_count):
#     try:
#         person_count = int(input("请输入人数:"))
#         result = apple_count / person_count
#         print(f"每人{result}个苹果")
#     except Exception:
#         print("程序出错啦")
#     else:
#         print("分苹果成功了")


div_apple(10)

print("后续逻辑")
