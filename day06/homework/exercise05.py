"""
    在终端中录入疫情地区名称，如果输入空字符串，则停止。
    如果录入的名称已经存在不要再次添加.
    最后倒序打印所有省份名称(一行一个)
"""
list_regions = []
while True:
    region = input("请输入疫情地区名称：")
    if region == "":
        break
    if region in list_regions:
        print("已经存在")
    else:
        list_regions.append(region)

for i in range(len(list_regions) - 1, -1, -1):
    print(list_regions[i])

# 通过切片读取数据,会触发浅拷贝,占用内存过多
# for item in list_regions[::-1]:
#     print(item)

