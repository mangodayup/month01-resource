"""
    练习：自定义降序排列算法
"""
list01 = [4,54,6,7,9,0]
# 降序 : 大 --> 小
# 1. 取数据
for r in range(len(list01)-1):#        0      1     2
    # 2. 作比较
    for c in range(r+1,len(list01)):# 12345  2345  345
        if list01[r] < list01[c]:
            list01[r],list01[c] =  list01[c],list01[r]
print(list01)