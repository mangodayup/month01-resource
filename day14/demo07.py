"""
    小结 - Python程序结构
        1. 为什么要有模块和包?
        答:便于团队开发,逻辑结构清晰.
        2. 导入方式
            "我过去"  import 路径.模块
                     import 路径.包
                     import 包
            "你过来"  from 模块 import 内容
                     from 路径.模块 import 内容
                     from 路径 import 模块
                     from 路径 import 包
            注意:import 包时候,__init__.py模块必须设置
        3. 导入是否成功
            导入路径 + 系统路径 = 真实路径
"""