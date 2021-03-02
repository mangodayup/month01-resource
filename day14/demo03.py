"""
    模块变量
"""
import random

# 1.__doc__ 存储当前模块的文档注释
# 在交互式python中使用
print(__doc__)


# 2. __name__ 存储模块名
# 当运行在主模块时,存储的是__main__
# 当运行在被导入模块时,存储的是真实模块名
print(__name__)
import demo02
