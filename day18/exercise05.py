"""
    修改装饰器使用方式
"""
def verif_permissions(func):
    def wrapper(*args,**kwargs):
        print("验证权限")
        return func(*args,**kwargs)

    return wrapper

@verif_permissions
def insert(data):
    print("插入",data)
    return 1001

@verif_permissions
def delete():
    print("删除")
    return True

print(insert("数据"))
print(delete())
