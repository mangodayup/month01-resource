"""
    拷贝:对数据进行备份,防止错误修改.
    浅拷贝:只备份一层
        优点:占用内存较少
        缺点:如果深层数据被修改,互相影响.
    深拷贝:备份所有层
        优点:绝对互不影响
        缺点:占用内存过多
    适用性:
        当没有深层数据或深层数据不会变化时使用浅拷贝
        否则使用深拷贝

"""
# 准备深拷贝工具
import copy

list01 = [10, [20, 30]]
list02 = list01[:] # 浅拷贝
list03 = copy.deepcopy(list01)# 深拷贝
list02[0] = 100
list02[1][0] = 200
print(list01)

list03[0] = 1000
list03[1][0] = 2000
print(list01)



