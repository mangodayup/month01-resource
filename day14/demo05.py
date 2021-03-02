"""
    包中__init__价值
        当客户端代码直接导入包时,自动执行__init__中的代码
        可以隐藏包内复杂的逻辑结构,在__init__中提供简单的使用方式
"""
# import 包
# 需要设置包的__init__.py模块
import package01.package02

package01.package02.module02.func01()

import package01

package01.func01()