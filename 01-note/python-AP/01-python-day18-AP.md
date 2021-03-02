# Day 18   2021/1/25  星期一

---

# 闭包

## 定义

是由函数及其相关的引用环境组合而成的实体。 

## 三要素

- 必须有一个内嵌函数。

- 内 嵌函数必须引用外部函数中变量。

- 外部函数返回值必须是内嵌函数。

```python
"""
    闭包
        作用：外部函数栈帧,执行过后不释放.
        字面意思：封闭 内存空间
        步骤：
            1. 有外有内
            2. 内使用外
            3. 外返回内
            【相当于套保鲜膜的步骤】
"""
# 1. 有外有内
def func01():
    a = 10   # 【剩菜】
    def func02(): # 【晚上...】
        # 2. 内使用外
        print(a)  #【吃】
    # 3. 外返回内
    # return func02() # 执行了内部函数,返回None
    return func02 # 不执行内部函数,只返回

# 调用外部函数,接收内部函数
re = func01()
# 通过返回值,不断调用内部函数
re()
re()
re()
```

## 语法

- def 外部函数名(参数):

  ​    外部变量

  ​    def 内部函数名(参数):

  ​        使用外部变量

  ​    return 内部函数名

- 调用：

     变量 = 外部函数名(参数)

     变量(参数)

## 优点和缺点

优点：内部函数可以使用外部变量。

缺点：外部变量一直存在于内存中，不会在调用结束后释放，占用内存。

## 作用

实现python装饰器。

## 应用

```python
"""
    闭包应用
        逻辑连续
            从获得压岁钱,
            到不断购买的过程不中断可持续
"""

def give_gife_money(money):
    print(f"获得了{money}元压岁钱")

    def child_buy(commodity, price):
        nonlocal money
        money -= price
        print(f"购买{commodity}花了{price},还剩下{money}")

    return child_buy


action = give_gife_money(1000)
action("遥控汽车", 300)
action("遥控飞机", 500)
action("变形金刚", 200)
```

## 内存图

<img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210126154812136.png" alt="image-20210126154812136" style="zoom:50%;" />

# 装饰器

## 参数思想

<img src="/Users/chenjingru/Library/Application Support/typora-user-images/image-20210126154838573.png" alt="image-20210126154838573" style="zoom:50%;" />

## 示例

```python
"""
    闭包最佳实践 - 装饰器
        1. 有外有内：外函数负责存储旧功能
        2. 内使用外：内函数负责执行新旧功能
        3. 外返回内：不断执行新与旧
        价值：
            可装可卸
"""


# 为旧功能(func01/func02)
# 增加新功能(new_func)
def func01():
    print("功能1")


def func02():
    print("功能2")


# 装饰器：
def new_func1(func):
    def wrapper():
        print("新功能1")  # 执行新功能
        func()  # 执行旧功能

    return wrapper


def new_func2(func):
    def wrapper():
        print("新功能2")  # 执行新功能
        func()  # 执行旧功能

    return wrapper


# 旧功能 = 新功能
# func01 = new_func # 覆盖了旧功能
# new_func(func01) # 此时执行了新旧功能

# 调用外函数包装新与旧
func01 = new_func1(func01)

# func02包装两种功能
func02 = new_func1(func02)
func02 = new_func2(func02)

# 调用内函数执行新与旧
func01()
func01()
func02()
func02()
```

## 定义

在不改变原函数的调用以及内部代码情况下，为其添加新功能的函数。

## 语法

def 函数装饰器名称(func):

​    def wrapper(*args, **kwargs):

​      需要添加的新功能

​      return func(*args, **kwargs)

  return wrapper

​            原函数 = 内嵌函数

​    @ 函数装饰器名称

​    def 原函数名称(参数):

​        函数体

​    原函数(参数)

## 本质

使用“@函数装饰器名称”修饰原函数，等同于创建与原函数名称相同的变量，关联内嵌函数；故调用原函数时执行内嵌函数。

原函数名称 = 函数装饰器名称（原函数名称）

 ## 装饰器链

一个函数可以被多个装饰器修饰，执行顺序为从近到远。