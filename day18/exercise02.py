"""
    在不改变旧功能(insert,delete)的定义与调用情况下,
    为其增加新功能(verif_permissions)
"""


def insert():
    print("插入")


def delete():
    print("删除")


def verif_permissions(func):
    def wrapper():
        print("验证权限")
        func()

    return wrapper


# insert = verif_permissions # 覆盖旧功能
# verif_permissions(insert) # 提前执行了新旧功能
insert = verif_permissions(insert)
delete = verif_permissions(delete)

insert()  # 执行新旧功能
delete()
