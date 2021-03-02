"""
    字符串字面值
"""
# 1. 不同写法
str01 = "悟空"
str02 = '悟空'
# 可见即所得
str03 = '''悟空'''
str03 = """
    悟

空"""
print(str03)

# 2. 引号冲突
print('我是"悟空"同学')
print("我是'悟空'同学")
print("""我'是'悟"空"同学""")

# 3. 转义符:改变原始含义的符号
# \"  \'  \\  \n换行
print("我是\"悟空\"同学")
print("我是\n悟空同学")

print("c:a\\b\\a\d.txt")
# 原始字符
print(r"c:a\b\a\d.txt")

# 4. 字符串格式化
# 适用性:在固定格式中,插入变量.
# 语法:
#   "..占位符.."%(变量)
# 占位符
#   %s 字符串   %d 整数  %f 小数
#   %.2d 两位整数,不足在前面用0填充
#   %.2f 四舍五入保留两位小数

subject = "I"
predicate = "kiss"
object = "you"
# 字符串拼接
# print("您输入的主语是:" + subject + ",谓语是:" + predicate + ",宾语是:" + object)
print("您输入的主语是:%s,谓语是:%s,宾语是:%s" % (subject, predicate, object))

rate = 5
# print("治愈比例为" + str(rate) + "%")
print("治愈比例为%.2d%%" % rate)
print("价格%.2f元" % (5 / 3))
