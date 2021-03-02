"""
    修改装饰器使用方式
"""
def verif_permissions(func):
    def wrapper():
        print("验证权限")
        func()

    return wrapper

@verif_permissions
# insert = verif_permissions(insert)
def insert():
    print("插入")

@verif_permissions
# delete = verif_permissions(delete)
def delete():
    print("删除")

insert()
delete()
