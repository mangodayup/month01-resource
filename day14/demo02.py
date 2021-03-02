"""
    模块 module
"""
print(__name__)
# 方式一:"我过去"
# 本质:创建变量关联模块地址
# 语法:import 模块名
import module01

module01.func01()

# 方式二 :"你过来"
# 本质: 将目标模块成员导入到当前模块作用域中
# 语法:from 模块名 import 内容
# 注意:命名冲突,可使用as定义别名

from module01 import func01 as f1
from module01 import func02,func03
from module01 import *

def func01():
    print("demo02的func01")

func01()
f1()
func05()