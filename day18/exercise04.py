"""
    修改装饰器使用方式
"""
def verif_permissions(func):
    def wrapper():
        print("验证权限")
        return func()

    return wrapper

@verif_permissions
def insert():
    print("插入")
    return 1001

@verif_permissions
def delete():
    print("删除")
    return True

print(insert()) # 1001
print(delete()) # True
