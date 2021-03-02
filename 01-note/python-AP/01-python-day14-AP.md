# Day 14   2021/1/19  星期二

---

# 模块 Module

## 定义

包含一系列数据、函数、类的文件，通常以.py结尾。

- 让一些相关的数据，函数，类有逻辑的组织在一起，使逻辑结构更加清晰。

- 有利于多人合作开发。

## 导入

标蓝（设置项目根目录）：文件夹右键--mark directory as--sources root

```python
#module_exercise.py
data = 100
def func01():
    print("func01执行喽")
class MyClass:
    def func02(self):
        print("func02执行喽")
    @classmethod
    def func03(cls):
        print("func03执行喽")
```

### 方式一

import 模块名 更适合面向过程

- 作用：将模块内的一个或多个成员导入到当前模块的作用域中。

- 使用：直接使用成员名

```python
import module_exercise
print(module_exercise.data)
module_exercise.func01()
m = module_exercise.MyClass()
m.func02()
module_exercise.MyClass.func03()
```

### 方式二

from 模块名 import 方法名 [as 别名]（*）更适合面向对象

- 作用：将某模块整体导入到当前模块中。

- 使用：模块名.成员

```python
from module_exercise import *

print(data)
func01()
m = MyClass()
m.func02()
MyClass.func03()
```

### 快捷键

mac：option+回车

windows：alt+回车

## 项目架构

（1）创建目录student_info_manager_system

（2）创建模块bll,存储XXController    业务逻辑层 business logic layer

（3）创建模块usl,存储XXView    用户显示层 user show layer

（4）创建模块model,存储XXModel

（5）创建模块main,存储调用XXView的代码

只有被导入的模块才会生成pyc文件

main（主模块：第一次执行的入口代码）不会生成pyc，如果将其和其他代码放在一起，就没法优化了，所以主模块尽量简洁，能少写则少写

## 模块变量

\_\_doc\__变量：文档字符串。

\__name__变量：模块自身名字，可以判断是否为主模块。

当此模块作为主模块(第一个运行的模块)运行时，__name__绑定'__main__'，不是主模块，而是被其它模块导入时,存储模块名。

在模块导入时，模块的所有语句会执行。

如果一个模块已经导入，则再次导入时不会重新执行模块内的语句。



main 快捷键

Command + P        参数信息（在方法中调用参数）

Ctrl + J       快速查看文档

Ctrl + Alt + M  提取方法

shift+command+L 改名



## 分类

1. 内置模块(builtins)，在解析器的内部可以直接使用。

2. 标准库模块，安装Python时已安装且可直接使用。

3. 第三方模块（通常为开源），需要自己安装。

4. 用户自己编写的模块（可以作为其他人的第三方模块）

# 包 package

项目根目录

包

​			模块

​						类

​								函数

​											语句

## \__init__.py 文件

import包，需要设置包的\__init.py__文件  

是包内必须存在的文件

会在包加载时被自动调用

作用：当客户端代码直接导入包时，自动执行\_\_init\_\_.py中的代码，可以隐藏包内复杂的逻辑结构，在\__init.py__中提供简单的使用方式

## 根目录

主模块所在文件夹是根目录

```python
import sys

print(sys.path)
```

## time

```python
import time

#获取当前机器时间——时间戳（单位是秒）

time.time()

#获取当前人类时间——时间是元组（年/月/日/时/分/秒/一周第几天/一年第几天/夏令时）

time.localtime()

#时间戳转为时间元组

time.localtime(时间戳)

#时间元组转为时间戳
time.mktime(time_tuple)

#时间元组转换成字符串
time.strftime("%y-%m-%d %H:%M:%S",time_tuple)
#字符串转换成时间元组
print(time.strptime("21-10-12 16:06:11","%y-%m-%d %H:%M:%S"))
# %Y 代表2021
```