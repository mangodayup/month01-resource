"""
# 练习2：
# 循环录入编码值打印文字，直到输入空字符串停止。
"""
while True:
    code_value = input("请输入编码值:")
    if code_value == "":
        break
    print(chr(int(code_value)))
