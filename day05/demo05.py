"""
    列表
        删除
"""
list_name = ["纪添皓", "沙忠金", "熊志鹏"]
# -- 根据元素移除
# 列表名.remove(元素)
# 注意:如果元素不在,错误
if "沙忠金" in list_name:
    list_name.remove("沙忠金")
# -- 根据定位移除
del list_name[-1]
del list_name[:]
print(list_name)
