"""
    算法1:变量交换
    算法2:找最值
"""

bridegroom_name = "武大郎"
bride_name = "潘金莲"
# 方式一
# temp = bridegroom_name
# bridegroom_name = bride_name
# bride_name = temp
# 方式二  a ,b = b ,a
bridegroom_name, bride_name = bride_name, bridegroom_name
print("交换后的新郎：" + bridegroom_name)  # ?
print("交换后的新娘：" + bride_name)  # ?
