"""
    运算符
        增强运算符
            在算数运算符基础上,对自身赋值
            +=  -= *=  /=  //=  %=  **=
"""
data01 = 10
# 相加产生新数据,但不影响旧数据
# data01 + 5
# data01 = data01 + 5
data01 += 5 # 累加
print(data01)  # 15
