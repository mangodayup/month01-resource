"""
    练习1：
    创建2个模块module_exercise.py与exercise.py
        将下列代码粘贴到module_exercise模块中，并在exercise中调用。
"""
# 标蓝(设置项目根目录)
# 文件夹右键 - Mark Directory - Sources Root
# 方式1:适合面向过程(全局变量/函数)
import module_exercise

print(module_exercise.data)
module_exercise.func01()
m01 = module_exercise.MyClass()
m01.func02()
module_exercise.MyClass.func03()

# 方式2: 适合面向对象(类)
from module_exercise import *

print(data)
func01()
m02 = MyClass()
m02.func02()
MyClass.func03()
