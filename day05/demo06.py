"""
    列表内存图
        定位
"""
list01 = [10, 20, 30]
data01 = list01  # 赋值
data02 = list01[0]  # 索引
data03 = list01[:2]  # 切片

data01[0] = 100
data03[-2:] = [200,300]
print(list01) # ?
