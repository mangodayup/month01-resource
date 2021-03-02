"""
    列表
        定位
        遍历
"""
list_name = ["纪添皓", "沙忠金", "熊志鹏"]
# 1. 定位
# -- 索引
print(list_name[1])
list_name[1] = "老金"
# -- 切片
# 切片读取原理:创建新列表(拷贝/复制/备份)
print(list_name[:2])
# 切片修改原理:遍历右侧可迭代数据,依次存入左侧区域
# 左侧定位2  右侧存入2
list_name[:2] = ["小纪","小金"]
# 左侧定位0  右侧存入2
# list_name[1:1] = ["小纪","小金"]
# 左侧定位2  右侧存入0
# list_name[:2] = []
# 报错
# list_name[:2] = 100

# 2. 遍历
# -- 从头到尾读取数据
for item in list_name:
    print(item)

# -- 非从头到尾读取数据
# for i in range(len(list_name)):
#     # if 条件:
#     list_name[i] = "xx"

# 开始:总数-1
# 结束:range不包含-1,实际包含的是0
# 间隔:倒序
for i in range(len(list_name)-1,-1,-1):
    print(list_name[i])